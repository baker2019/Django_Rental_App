from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import uuid


class UserManager(BaseUserManager):
    """This is the Object Manager for the User Model

    Arguments:
        serializers {ModelSerializer} -- Django builtin Serializer
    """
    def create_user(self, email, password, first_name=None, last_name=None,
                    is_active=True, is_staff=False, is_admin=False):
        """Creates a User instance

        Arguments:
            email {string} -- email of the new user
            password {string} -- password of the new user

        Keyword Arguments:
            first_name {string} -- Full name of the new user (default: {None})
            last_name {string} -- Full name of the new user (default: {None})
            is_active {bool} -- Status if the user is active (default: {True})
            is_staff {bool} -- Status if the user is staff (default: {False})
            is_admin {bool} -- Status if the user is admin (default: {False})

        Raises:
            ValueError: If there is no email
            ValueError: If there is no password

        Returns:
            User -- Returns the new user instance
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.first_name = first_name,
        user.last_name = last_name,
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None,
                         first_name=None, last_name=None):
        """Creates a Superuser

        Arguments:
            email {string} -- email address of the superuser

        Keyword Arguments:
            password {string} -- password of the superuser (default: {None})
            full_name {string} -- Full name of the superuser (default: {None})

        Returns:
            [type] -- [description]
        """
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """The User model for each registered user

    Arguments:
        models {Model} -- Django builtin Model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255, unique=True
    )
    first_name = models.CharField(
        max_length=60, default=None, blank=True, null=True)
    last_name = models.CharField(
        max_length=60, default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        """Retreives the full name of a User

        Returns:
            string -- Full name of the User
        """
        return self.full_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin


class Host(models.Model):
    """Profile for Hosts"""
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
    )
    email = models.EmailField()
    superhost = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # customer_id for Stripe

    def __str__(self):
        """__str__"""
        return self.id
