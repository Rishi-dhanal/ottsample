from django import forms
from .models import Register, User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['username', 'email', 'password', 'age_limit', 'gender']

        widgets = {
            'password': forms.PasswordInput(),
        }
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name','email', 'profile_picture']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
