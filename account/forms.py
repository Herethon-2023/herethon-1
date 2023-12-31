from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth.forms import PasswordResetForm as BasePasswordResetForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'nickname', 'school_name', 'school_photo']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(UserChangeForm) :
    class Meta :
        model = User
        fields = ['user_profile', 'username', 'name', 'nickname', 'email', 'school_name', 'school_photo']

class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail'})
    )
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'New Password'})
    )
    new_password2 = forms.CharField(
        label="Password Check",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password Check'})
    )

