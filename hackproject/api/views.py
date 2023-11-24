from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import get_classrooms, get_classroom, create_classroom, update_classroom, delete_classroom

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/classrooms/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of classrooms'
        },
        {
            'Endpoint': '/classrooms/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single classroom'
        },
        {
            'Endpoint': '/classroom/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new classroom with data sent in post request'
        },
        {
            'Endpoint': '/classroom/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing classroom with data sent in put request'
        },
        {
            'Endpoint': '/classroom/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an exiting classroom'
        },
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
def get_classrooms_view(request):

    if request.method == 'GET':
        return get_classrooms(request)

    if request.method == 'POST':
        return create_classroom(request)


@api_view(['GET', 'PUT', 'DELETE'])
def get_classroom_view(request, pk):

    if request.method == 'GET':
        return get_classroom(request, pk)

    if request.method == 'PUT':
        return update_classroom(request, pk)

    if request.method == 'DELETE':
        return delete_classroom(request, pk)