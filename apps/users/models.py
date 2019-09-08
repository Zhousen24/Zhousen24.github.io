from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as _UserManager

# Create your models here.

class UserManager(_UserManager):           # 方法重写

    def create_superuser(self, username, password, email=None, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    # 
    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError('Superuser must have is_staff=True.')
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError('Superuser must have is_superuser=True.')
    # 
    #     return self._create_user(username, email, password, **extra_fields)
        # 调用super方法继承auth/models.py的create_superuser方法
        super().create_superuser(username=username, password=password, email=email, **extra_fields)


class User(AbstractUser):       # 类方法空两行
    """
    add mobile  \email_active fields to Django users models
    """

    objects = UserManager()

    REQUIRED_FIELDS = ['mobile',]        # 指定注册账户

    mobile = models.CharField(max_length=11, unique=True, verbose_name='telephone number', help_text='telephone number', error_messages={'unique': "此号码已经注册"})

    email_active = models.BooleanField(default=False, verbose_name='邮箱验证状态')

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name      # 显示的复数名称

    def __str__(self):
        return self.username
