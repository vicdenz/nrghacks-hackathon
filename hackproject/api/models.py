from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Classroom(models.Model):
	REPORT_REGULARITY_CHOICES = (
		("D", "Daily"),
		("W", "Weekly"),
		("M", "Monthly"),
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="classroom")

	grade_level = models.PositiveIntegerField(
		verbose_name="Grade Level",
		validators=[
            MaxValueValidator(15),
            MinValueValidator(1)
        ]
	)

	class_name = models.CharField(
		verbose_name="Class Name",
		max_length=30,
	)

	instant_alert = models.BooleanField(
		verbose_name="Instant Alert",
	)

	report_regularity = models.CharField(
		verbose_name="Regularity Of Reports",
		choices=REPORT_REGULARITY_CHOICES,
		max_length=20,
	)

class Student(models.Model):
	GENDER_CHOICES = (
		("M", "Male"),
		("F", "Female"),
	)

	first_name = models.CharField(
		verbose_name="First Name",
		max_length=40,
	)

	last_name = models.CharField(
		verbose_name="Last Name",
		max_length=80,
	)

	grade = models.IntegerField(
		verbose_name="Grade",
	)

	gender = models.CharField(
		verbose_name="Gender",
		choices=GENDER_CHOICES,
		blank=True,
		max_length=6,
	)

	parent_email = models.EmailField(
		verbose_name="Parent Email",
		blank=True,
	)

	classrooms = models.ForeignKey(Classroom, on_delete=models.PROTECT, related_name="classroom")

class Section:
	classrooms = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="classroom")

	title = models.CharField(
		verbose_name="Title",
		max_length=20,
	)

	rank = models.IntegerField(
		verbose_name="Rank",
	)