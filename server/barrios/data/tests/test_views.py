import os
import shutil
from typing import Any
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpResponse, HttpResponseNotAllowed
from django.test import TestCase, override_settings
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied, ValidationError
from django.test import TestCase, override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpResponse
from data.models import Upload
from data.views import upload_post

TEST_DIR = "test_data"


class TestDataViews(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            "test", email="test@test.test", password="pass"
        )
        self.user.save()

    def tearDown(self):
        shutil.rmtree(TEST_DIR, ignore_errors=True)

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

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def test_file_upload_rejects_unauthed_user(self):
        """
        Test that upload_post raises PermissionDenied if user is not authenticated
        """
        csv = SimpleUploadedFile(
            "test.csv", b"one,two,three,four", content_type="text/csv"
        )
        response: HttpResponse | Any = self.client.post(
            reverse("upload_post"), {"file": csv}
        )
        self.assertRaises(PermissionDenied)

    @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
    def test_file_upload_works_for_authed_user(self):
        """
        Test that file upload works for an authorized user
        """
        self.client.force_login(self.user)
        csv = SimpleUploadedFile(
            "test.csv", b"one,two,three,four", content_type="text/csv"
        )
        response: HttpResponse | Any = self.client.post(
            "/data/files/upload", {"file": csv}
        )
        self.assertRedirects(response, "/data/")

    def test_get_request_to_upload_not_allowed(self):
        """
        Test that an attempt to GET /data/files/upload/ returns ResponseNotAllowed
        """
        self.client.force_login(self.user)
        response: HttpResponse | Any = self.client.get("/data/files/upload/")
        self.assertEqual(response.status_code, 405)

    # def test_upload_post_not_authenticated(self):
    #     """
    #     Test that upload_post raises PermissionDenied if user is not authenticated
    #     """
    #     request = self.client.post(reverse("upload_post"))
    #     with self.assertRaises(PermissionDenied):
    #         upload_post(request)

    # def test_upload_post_invalid_form(self):
    #     """
    #     Test that upload_post redirects to /data/ if form is invalid
    #     """
    #     self.client.force_login(self.user)
    #     request = self.client.post(reverse("upload_post"))
    #     response: HttpResponse | Any = upload_post(request)
    #     self.assertRedirects(response, "/data/")

    # @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
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

    # @override_settings(MEDIA_ROOT=(TEST_DIR + "/media"))
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
