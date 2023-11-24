from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import updateNote, getNoteDetail, deleteNote, getNotesList, createNote

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
def getNotes(request):

    if request.method == 'GET':
        return getNotesList(request)

    if request.method == 'POST':
        return createNote(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):

    if request.method == 'GET':
        return getNoteDetail(request, pk)

    if request.method == 'PUT':
        return updateNote(request, pk)

    if request.method == 'DELETE':
        return deleteNote(request, pk)