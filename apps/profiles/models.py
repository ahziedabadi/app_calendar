from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")
    RATHER_NOT_TO_SAY = "Rather_not_to_say", _("Rather_not_to_say")


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+41524204242"
    )
    about_me = models.TextField(verbose_name=_("About_me"), default="Say something.")
    profile_avatar = models.ImageField(
        verbose_name=_("Profile_photo"), default="/profile_default.png"
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.RATHER_NOT_TO_SAY,
        max_length=20,
    )

    def __str__(self):
        return f"{self.user.username}'s profile"
