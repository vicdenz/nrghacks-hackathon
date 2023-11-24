from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=35, required=False)
    last_name = forms.CharField(max_length=35, required=False)
    email = forms.EmailField(max_length=254, required=True, help_text='Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class ProfileSignupForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)
    phone_number = forms.CharField(required=False, help_text='Enter a valid phone number.', widget=forms.TextInput(attrs={'placeholder': '(123)-456-7890'}))
    address = forms.CharField(required=False)
    birthdate = forms.DateField(required=False)

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'phone_number', 'address', 'birthdate']

    # def clean_profile(self):
    #     avatar = self.cleaned_data['avatar']

    #     try:
    #         w, h = get_image_dimensions(avatar)

    #         #validate dimensions
    #         max_width = max_height = 100
    #         if w > max_width or h > max_height:
    #             raise forms.ValidationError(
    #                 u'Please use an image that is '
    #                  '%s x %s pixels or smaller.' % (max_width, max_height))

    #         #validate content type
    #         main, sub = avatar.content_type.split('/')
    #         if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
    #             raise forms.ValidationError(u'Please use a JPEG, '
    #                 'GIF or PNG image.')

    #         #validate file size
    #         if len(avatar) > (20 * 1024):
    #             raise forms.ValidationError(
    #                 u'Avatar file size may not exceed 20k.')

    #     except AttributeError:
    #         """
    #         Handles case when we are updating the user profile
    #         and do not supply a new avatar
    #         """
    #         pass

    #     return avatar