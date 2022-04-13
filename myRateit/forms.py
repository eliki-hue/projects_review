
from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Project, Comment,Rate

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['username']
        fields ='__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude=['author']
        fields ='__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields='__all__'

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



class RateForm(forms.ModelForm):
   
    class Meta:
        model:Rate
        field = '__all__'