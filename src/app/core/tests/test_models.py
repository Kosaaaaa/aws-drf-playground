"""
Tests for models
"""

from django.contrib.auth import get_user_model
from django.test import TestCase


def create_user(email="user@example.com", password="testPass123"):
    """Create a return a new user."""
    return get_user_model().objects.create_user(email, password)


class UserModelTests(TestCase):
    """Test User model"""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = "test@example.com"
        password = "testPass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.com", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaisesRegex(ValueError, r"email"):
            get_user_model().objects.create_user("", "test123")

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "test123",
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_user_with_falsy_password(self):
        """Test creating user with falsy password"""
        email = "test@example.com"

        for password in (None, False, 0, ""):
            with self.assertRaisesRegex(ValueError, r"password"):
                get_user_model().objects.create_user(email, password)

    def test_user_soft_delete(self):
        user = create_user()
        user.soft_delete()

        self.assertTrue(user.is_deleted)
        self.assertIsNotNone(user.deleted_at)

    def test_users_uuid_unique(self):
        sample_emails = [
            "test1@example.com",
            "test2@example.com",
            "test3@example.com",
            "test4@example.com",
        ]

        user_uuids = []

        for email in sample_emails:
            user = create_user(email)
            user_uuids.append(user.uuid)

        self.assertEqual(len(user_uuids), len(set(user_uuids)))
