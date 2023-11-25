from rest_framework.response import Response
from .models import Classroom
from .serializers import ClassroomSerializer

def get_classrooms(request):
    classrooms = Classroom.objects.all().order_by('grade')
    serializer = ClassroomSerializer(classrooms, many=True)
    return Response(serializer.data)

def get_classroom(request, pk):
    classroom = Classroom.objects.get(id=pk)
    serializer = ClassroomSerializer(classroom, many=False)
    return Response(serializer.data)

def create_classroom(request):
    data = request.data
    note = Classroom.objects.create(
        body=data['body']
    )
    serializer = ClassroomSerializer(note, many=False)
    return Response(serializer.data)

def update_classroom(request, pk):
    data = request.data
    classroom = Classroom.objects.get(id=pk)
    serializer = ClassroomSerializer(instance=classroom, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def delete_classroom(request, pk):
    classroom = Classroom.objects.get(id=pk)
    classroom.delete()
    return Response('Classroom was deleted!')