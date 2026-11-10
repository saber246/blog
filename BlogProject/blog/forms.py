from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label = '邮箱',
        required = True,
        help_text = '请输入有效的邮箱地址'
    )
    class Meta: # type: ignore
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {  # noqa: RUF012
            'username': '用户名',
            'password1': '密码',
            'password2': '确认密码'
        }
        help_texts = {  # noqa: RUF012
            'username': '',
            'password1': '',
            'password2': '',
            'email': ''
        }
        