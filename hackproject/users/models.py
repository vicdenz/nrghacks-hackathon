import os, datetime
from django.utils.text import slugify

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.

UPLOAD_PATH = "images/profiles"

class UserProfile(models.Model):
	def generate_upload_path(self, filename):
		username = self.user.username  # Get the username of the user
		filename, ext = os.path.splitext(filename.lower())
		filename = f"{slugify(username)}_{datetime.datetime.now().strftime('%Y-%m-%d.%H-%M-%S')}{ext}"
		return f"{UPLOAD_PATH}/{filename}"

	user = models.OneToOneField(User, on_delete=models.CASCADE)

	profile_picture = models.ImageField(
		verbose_name="Profile picture",
		upload_to=generate_upload_path,
		null=True,
		blank=True,
	)

	phone_number = models.CharField(
		verbose_name="Phone number",
		max_length=15,
		help_text="Phone number in the format (123)-456-7890.",
		validators=[
			RegexValidator(
				regex=r'^\(\d{3}\)-\d{3}-\d{4}$',
				message="Enter a valid phone number in the format (123)-456-7890.",
				code="invalid_phone_number",
			),
		],
		null=True,
		blank=True,
	)

	updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True, null=True, blank=True)