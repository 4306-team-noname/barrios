from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.contrib.auth import get_user_model


class TestDataViews(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            "test", email="test@test.test", password="pass"
        )
        self.user.save()

    def test_user_not_authenticated_base_route(self):
        """Check that a non-authenticated user is redirected from /data/"""
        response = self.client.get("/data/")
        self.assertEqual(response.status_code, 302)

    def test_user_authenticated_base_route(self):
        """
        Check that an authenticated user receives status 200 from /data/
        """
        self.client.force_login(self.user)
        response = self.client.get("/data/")
        self.assertEqual(response.status_code, 200)

    def test_file_upload_rejects_unauthed_user(self):
        """
        Check that an unauthorized user can't upload a file
        """
        csv = SimpleUploadedFile(
            "test.csv", b"one,two,three,four", content_type="text/csv"
        )
        response = self.client.post("/data/upload/", {"file": csv})
        self.assertEqual(response.status_code, 403)

    def test_file_upload_works_for_authed_user(self):
        """
        Check that file upload works for an authorized user
        """
        self.client.force_login(self.user)
        csv = SimpleUploadedFile(
            "test.csv", b"one,two,three,four", content_type="text/csv"
        )
        response = self.client.post("/data/upload/", {"file": csv})
        self.assertEqual(response.status_code, 200)

    # TODO: Add a validator to the Upload model. While
    # the FileExtensionValidator can be used, we need to find
    # a way to ensure the file contents are what we expect as well
    # either way, the view is not the place to check that this validation
    # works properly.
    #
    # def test_upload_non_csv_file_fails(self):
    #     """
    #     Check that uploading non-csv files fails
    #     """
    #     self.client.force_login(self.user)
    #     not_csv = SimpleUploadedFile(
    #         "test.txt", b"This is text", content_type="text/plain"
    #     )
    #     response = self.client.post("/data/upload/", {"file": not_csv})
    #     self.assertEqual(response.status_code, 422)

    def test_get_request_to_upload_redirects_to_data(self):
        """
        Check that an attempt to GET /data/upload/ redirects to /data/
        """
        self.client.force_login(self.user)
        response = self.client.get("/data/upload/")
        self.assertRedirects(
            response,
            "/data/",
            status_code=302,
            target_status_code=200,
            msg_prefix="",
            fetch_redirect_response=True,
        )
