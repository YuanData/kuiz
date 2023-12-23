from django import forms
from django.contrib.auth.models import User

from . import models


class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def __init__(self, *args, **kwargs):
        super(StudentUserForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].required = False


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['address', 'mobile', 'profile_pic']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
