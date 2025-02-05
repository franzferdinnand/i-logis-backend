from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import CharField, BooleanField, EmailField, PositiveSmallIntegerField
from phonenumber_field.modelfields import PhoneNumberField

from users.managers import UserManager


class User(AbstractBaseUser):
    email = EmailField(unique=True)
    first_name = CharField(max_length=100, null=True)
    last_name = CharField(max_length=100, null=True)
    phone_number = PhoneNumberField(region="PL")
    role = PositiveSmallIntegerField(null=True)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number"]

    class Meta:
        db_table = "users"
        ordering = ["-id"]

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        if self.last_name:
            return f"{self.first_name} {self.last_name}".title()
        return self.first_name.title()
