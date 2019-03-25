from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        exclude = ["user"]

class UserProfileUpdateForm(forms.ModelForm):
    """Update user profile information."""
    avatar = fields.ImageField(upload_to='uploads/')
    dob = forms.DateTimeField(label='Date of Birth',
                            input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'],
                            widget=forms.SelectDateWidget(
                                years=range(1917,2017)
                            )
    )
    bio = forms.CharField(max_length=140, label='Biography',
                    widget=forms.Textarea(attrs={'rows': 6}), min_length=10)
    location = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={'placeholder': 'Enter current location'}),
    
    
    )
    hobby = forms.CharField(
        max_length=40,
        label='Favorite Hobby',
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter your favorite hobby'}
        )
    )

    class Meta:
        model = Profile
        fields = ['avatar', 'dob', 'bio', 'location', 'hobby']
        labels = {
            'avatar': ('Your Photo'),
        }

class UserUpdateForm(forms.ModelForm):
    """Form for updating user basic information."""
    verify_email = forms.EmailField(label="Please verify your email address.")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'verify_email']

    def clean(self):
        data = self.cleaned_data
        email = data.get('email')
        verify = data.get('verify_email')

        if email != verify:
            raise forms.ValidationError(
                "You need to enter the same email in both fields"
            )
