from django.test import TestCase
from users.models import UserInformation
from django.db.utils import IntegrityError


class TestUSerInformationModel(TestCase):
    def setUp(self):
        self.user1_information = UserInformation.objects.create(
            first_name="Miracle",
            email="miracle119@mail.com",
            hobbies="Football",
            about_me="I love watching Football",
        )

    def test_user_information_is_collected_and_saved(self):
        """
        Test user information is collected and saved
        """
        self.assertEqual(self.user1_information.first_name, "Miracle")
        self.assertEqual(self.user1_information.email, "miracle119@mail.com")
        self.assertEqual(self.user1_information.hobbies, "Football")
        self.assertEqual(self.user1_information.about_me, "I love watching Football")

    def test_user_information_is_collected_and_not_saved_if_email_exist(self):
        """
        Test user information is collect and saved when
        """
        with self.assertRaises(IntegrityError):
            user2_information = UserInformation.objects.create(
                first_name="james",
                email="miracle119@mail.com",
                hobbies="Football",
                about_me="I love watching Football",
            )

            self.assertIsNone(user2_information)
