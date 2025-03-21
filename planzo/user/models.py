from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        user = self.create_user(
            email,
            date_of_birth=date_of_birth,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  # Required for Django Admin
    is_superuser = models.BooleanField(default=False)
    is_varified = models.BooleanField(default=True)
    verication_secret = models.CharField(max_length=100, blank=True, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth"]

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True, null=True)



    def __str__(self):
        return self.user.email
