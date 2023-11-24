from rest_framework.serializers import ModelSerializer
from .models import Classroom, Student, Section

class StudentSerializer(ModelSerializer):
	class Meta:
		model = Student
		fields = '__all__'

class SectionSerializer(ModelSerializer):
	class Meta:
		model = Section
		fields = '__all__'

class ClassroomSerializer(ModelSerializer):
    students = StudentSerializer()
    author = SectionSerializer()

    class Meta:
        model = Classroom
        fields = '__all__'