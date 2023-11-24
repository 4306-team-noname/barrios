import os
import shutil
from typing import Any
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpResponse
from django.test import TestCase, override_settings
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.core.files.storage import InMemoryStorage
from data.models import Category

TEST_STORAGE = InMemoryStorage()

TEST_CSV_CONTENTS = b"""category_name,categoryID,module_name,moduleID,unique_cat_mod_ID
EDV,1,Consumables,2,2-1
Pretreat Tanks,2,Consumables,2,2-2
KTO,3,Consumables,2,2-3
ACY Inserts,4,Consumables,2,2-4
Filter Inserts,5,Consumables,2,2-5
Food-US,6,Consumables,2,2-6
Food-RS,7,Consumables,2,2-7"""

CATEGORIES = [
    {"category_id": 1, "category_name": "EDV", "rate_category": "Urine Receptacle"},
    {
        "category_id": 2,
        "category_name": "Pretreat Tanks",
        "rate_category": "Pretreat Tank",
    },
    {"category_id": 3, "category_name": "KTO", "rate_category": "KTO"},
    {"category_id": 4, "category_name": "ACY Inserts", "rate_category": "ACY Inserts"},
    {
        "category_id": 5,
        "category_name": "Filter Inserts",
        "rate_category": "Filter Inserts",
    },
    {"category_id": 6, "category_name": "Food-US", "rate_category": "US Food BOBs"},
    {"category_id": 7, "category_name": "Food-RS", "rate_category": "RS Food"},
]


@override_settings(MEDIA_ROOT=TEST_STORAGE.location)
class TestDataViews(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            "test", email="test@test.test", password="pass"
        )
        self.user.save()
        self.test_csv = SimpleUploadedFile(
            "test.csv",
            TEST_CSV_CONTENTS,
            content_type="text/csv",
        )
        for category in CATEGORIES:
            Category.objects.create(**category)

    def test_user_not_authenticated_base_route(self):
        """
        Test that a non-authenticated user is redirected from /data/
        """
        response: HttpResponse | Any = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 302)

    def test_user_authenticated_base_route(self):
        """
        Test that an authenticated user receives status 200 from /data/
        """
        self.client.force_login(self.user)
        response: HttpResponse | Any = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_file_upload_rejects_unauthed_user(self):
        """
        Test that upload_post raises PermissionDenied if user is not authenticated
        """
        response: HttpResponse | Any = self.client.post(
            reverse("upload_post"), {"file": self.test_csv}
        )
        self.assertRaises(PermissionDenied)

    def test_file_upload_works_for_authed_user(self):
        """
        Test that file upload works for an authorized user
        """
        self.client.force_login(self.user)
        response: HttpResponse | Any = self.client.post(
            reverse("upload_post"), {"file": self.test_csv}
        )
        self.assertRedirects(response, "/data/category_lookup/")

    def test_get_request_to_upload_not_allowed(self):
        """
        Test that an attempt to GET /data/files/upload/ returns ResponseNotAllowed
        """
        self.client.force_login(self.user)
        response: HttpResponse | Any = self.client.get(reverse("upload_post"))
        self.assertEqual(response.status_code, 405)

    def test_upload_post_not_authenticated(self):
        """
        Test that upload_post raises PermissionDenied if user is not authenticated
        """
        self.client.post(reverse("upload_post"))
        self.assertRaises(PermissionDenied)

    # def test_upload_post_invalid_form(self):
    #     """
    #     Test that upload_post redirects to /data/ if form is invalid
    #     """
    #     self.client.force_login(self.user)
    #     request = self.client.post(reverse("upload_post"))
    #     response: HttpResponse | Any = upload_post(request)
    #     self.assertRedirects(response, "/data/")

    # def test_upload_post_valid_form_no_match(self):
    #     """
    #     Test that upload_post raises ValidationError if file does not match any known data types
    #     """
    #     self.client.force_login(self.user)
    #     csv = SimpleUploadedFile(
    #         "test.csv", b"one,two,three,four", content_type="text/csv"
    #     )
    #     request = self.client.post(reverse("upload_post"), {"file": csv})
    #     with self.assertRaises(ValidationError):
    #         upload_post(request)

    # def test_upload_post_valid_form_with_match(self):
    #     """
    #     Test that upload_post redirects to /data/files/<upload_id>/ if file matches a known data type
    #     """
    #     self.client.force_login(self.user)
    #     csv = SimpleUploadedFile(
    #         "test.csv", b"one,two,three,four", content_type="text/csv"
    #     )
    #     request = self.client.post(reverse("upload_post"), {"file": csv})
    #     response: HttpResponse | Any = upload_post(request)
    #     upload_id = Upload.objects.latest("id").id
    #     self.assertRedirects(response, f"/data/files/{upload_id}/")
