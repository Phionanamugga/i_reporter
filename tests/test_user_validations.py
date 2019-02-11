import unittest
from api.models import User


class TestUser(unittest.TestCase):
    def setUp(self):
        kwargs = {
                "user_id": user_id,
                "firstname": data['firstname'],
                "lastname": data['lastname'],
                "email": data['email'],
                "phonenumber": data['phonenumber'],
                "username": data['username'],
                "password": data['password'],
                "registered_on": registered_on
            }
        self.user = User(**kwargs)

    def test_user_id(self):
        # Tests that the user_id is equal to the given id
        self.assertEqual(self.user.user_id, 1, "user_id must be 1")
        self.user.user_id = 2
        self.assertEqual(self.user.user_id, 2, "user_id is now 2")

    def test_user_id_type(self):
        # Tests the datatype of the user id
        self.assertNotIsInstance(self.user.user_id, str)
        self.assertIsInstance(self.user.user_id, int)

    def test_user_email(self):
        # Tests that the email is equal to the given email
        self.assertEqual(self.user.email, "email@gmail.com")

    def test_email_type(self):
        # Tests the datatype of the email
        self.assertIsInstance(self.user.email, str)
        self.assertNotIsInstance(self.user.email, int)

    def test_password(self):
        # Tests that the password is equal to the given password
        self.assertEqual(self.user.password, "1234567")
        self.user.password = "56784"
        self.assertEqual(self.user.password, "56784",
                         "password is now 56784")

    def test_class_instance(self):
        # Tests that the defined object is an instance of the User class
        self.assertIsInstance(self.user, User)