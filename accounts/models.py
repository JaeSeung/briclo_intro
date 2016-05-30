import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
# from django.contrib.auth.models import User


phone_number_validator = RegexValidator(r'^01[016789][1-9]\d{6,7}$', message='휴대폰 번호를 입력해주세요.')

def ktf_validator(phone_number):
    # 유효성 검사를 수행하기 전에, 먼저 값 가공
    phone_number = re.findall(r'\d+', phone_number)
    if phone_number[2] != '6':
        raise ValidationError('KTF 휴대폰 번호로 입력해주세요.')


class PhoneNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 20)
        kwargs.setdefault('validators', [])
        kwargs['validators'].append(phone_number_validator)
        kwargs['validators'].append(ktf_validator)
        super(PhoneNumberField, self).__init__(*args, **kwargs)


class Profile(models.Model):
    # user = models.OneToOneField(User)
    user = models.OneToOneField('auth.User')
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

