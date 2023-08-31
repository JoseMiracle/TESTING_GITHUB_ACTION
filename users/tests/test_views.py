from django.test import TestCase, Client
from users.models import UserInformation
from django.db.utils import IntegrityError
from django.urls import reverse

client = Client()


class TestInformationCollectedFromUser(TestCase):
    def setUp(self) -> None:
        self.url = reverse("users:collect-user-information")

    def test_user_information_is_collected_and_saved(self):
        """
        Test to confirm user information is collected
        """

        valid_information = {
            "first_name": "Miracle",
            "email": "josemiracle119@gmail.com",
            "hobbies": "Football",
            "about_me": "I'm Backend developer trying to learn more in the field",
        }
        response = client.post(path=self.url, data=valid_information, follow=True)
        self.assertEqual(response.status_code, 201)

        user_information = UserInformation.objects.filter(
            first_name=valid_information["first_name"],
            email=valid_information["email"],
            hobbies=valid_information["hobbies"],
            about_me=valid_information["about_me"],
        ).first()

        self.assertIsNotNone(user_information)
        self.assertTrue(user_information.first_name, valid_information["first_name"])

    def test_user_information_is_not_saved_when_email_provided_exists(self):
        """
        Tests user information isn't created when an similar email exists in the DB
        """
        UserInformation.objects.create(
            first_name="Delight",
            email="delight@mail.com",
            hobbies="Dancing",
            about_me="Love mettign new people",
        )

        invalid_information = {
            "first_name": "Miracle",
            "email": "delight@mail.com",
            "hobbies": "Football",
            "about_me": "I'm Backend developer trying to learn more in the field",
        }

        with self.assertRaises(IntegrityError):
            response = client.post(path=self.url, data=invalid_information) # noqa

            user_information = UserInformation.objects.filter(
                first_name=invalid_information["first_name"],
                email=invalid_information["email"],
                hobbies=invalid_information["hobbies"],
                about_me=invalid_information["about_me"],
            ).first()
            self.assertIsNone(user_information)
