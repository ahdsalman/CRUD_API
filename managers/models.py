from django.db import models
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# # Create your models here.

# class UserManager(BaseUserManager):
#     def create_superuser(self, email, first_name,last_name,username, password=None):
#         user = self.model(
#             email=self.normalize_email(email),
#             password=password,
#             first_name=first_name,
#             last_name=last_name,
#             username=username,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


# class Admin(AbstractBaseUser):

#     email = models.EmailField(verbose_name="email address",max_length=255,unique=True,)
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     username = models.CharField(max_length=200)
#     is_admin = models.BooleanField(default=True)
#     is_active =models.BooleanField(default=True)


#     obj = UserManager()

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["first_name","last_name","username"]


#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return self.is_admin