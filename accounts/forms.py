from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "email")


class SignupForm2(UserCreationForm):
    email = forms.EmailField()

    def save(self, commit=True):
        user = super(SignupForm2, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


def answer_validator(value):
    if value != 6:
        raise forms.ValidationError('땡~!!!')


class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='3+3=?')#, validators=[answer_validator])

    def clean_answer(self):
        '특정 필드에 대한 유효성 검사 및 값 변환'
        answer = self.cleaned_data.get('answer', None)
        if answer:
            if answer != 6:
                raise forms.ValidationError('땡~!!!!!!')
        return answer

    '''
    def clean(self):
        '다수 필드에 대한 유효성 검사 및 값 변환'
        username = self.cleaned_data.get('username', None)
        answer = self.cleaned_data.get('answer', None)
        if username and answer:
            if len(username) % 2 == 0 and answer % 2 == 0:
                raise forms.ValidationError('홀수로 입력하라구 !!!')
        return self.cleaned_data
    '''
