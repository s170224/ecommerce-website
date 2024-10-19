from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('This email is not given')
        email =self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        # print("hi")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)



class CustomUser(AbstractBaseUser):
    UserChoice = (
        (1,"Customer"),
        (2,"Business"),
        (2, "Admin")
    )

    email = models.EmailField(max_length=256, unique=True)
    first_name = models.CharField(max_length=256,  blank=True, null=True)
    last_name = models.CharField(max_length=246 , blank=True,null=True)
    user_type =models.SmallIntegerField(choices=UserChoice,null=True)
    phone_number = models.CharField(max_length=120, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=500,blank=True,null=True)
    pincode = models.CharField(max_length=120, blank=True,null=True)
    user_image = models.ImageField(upload_to='profile_images/',null=True,blank=True)
    is_superuser = models.BooleanField(default=False)
    is_active =models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


