# A Manager is the interface through which database query operations are provided to Django models.
# At least one Manager exists for every model in a Django application.
# The way Manager classes work is documented in Making queries;
# this document specifically touches on model options that customize Manager behavior.

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class CustomUserManager(BaseUserManager):
    """Manager for user."""

    def email_validator(self, email):
        """Validate email if its not a valid email raise error and return a message."""
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Please write a valid email."))

    def create_user(
        self, username, first_name, last_name, email, password, **extra_fields
    ):

        if not username:
            raise ValueError(_("This Field can not be empty."))

        if not first_name:
            raise ValueError(_("This Field can not be empty."))

        if not last_name:
            raise ValueError(_("This Field can not be empty."))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("An email address is required."))

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, first_name, last_name, email, password, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))

        if not password:
            raise ValueError(_("Superuser must have password"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("An email address is required."))

        user = self.create_user(username, first_name, last_name, email, password, **extra_fields)

        user.save(using=self._db)
        return user
