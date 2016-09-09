from .models import Student, Enroll
from django.contrib.auth.models import User
from django import forms
from django.forms import modelformset_factory

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('program_of_study',)


class EnrollForm(forms.ModelForm):
    class Meta:
        model = Enroll
        fields = ('semester','year','course_id','grade')
