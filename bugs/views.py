from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Bug
from .serializers import BugSerializer, ReadBugSerializer

# Create your views here.
#Retrieve single bug thru GET method
#Update single bug thru PUT method
@api_view(['GET', 'PUT'])
def get_update_bug(request, pk):
    try:
        bug = Bug.objects.get(pk=pk)
    except Bug.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # get details of a single bug
    if request.method == 'GET':
        serializer = BugSerializer(bug)
        return Response(serializer.data)
    # update details of a single bug
    elif request.method == 'PUT':
        data = {
            'title': request.data.get('title'),
            'desc': request.data.get('desc'),
            'is_open': request.data.get('is_open'),
            'handle_by': int(request.data.get('handle_by')),
            'created_by': bug.created_by.id,
            'updated_by': request.user.id,
        }
        serializer = BugSerializer(bug, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        else:
            #log error
            print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Retrieve all bugs thru GET method
#Create new bug thru POST method
@api_view(['GET', 'POST'])
def get_post_bugs(request):
    # get all bugs
    if request.method == 'GET':
        bugs = Bug.objects.all()
        serializer = ReadBugSerializer(bugs, many=True)
        return Response(serializer.data)
    # insert a new record for a bug
    elif request.method == 'POST':
        data = {
            'title': request.data.get('title'),
            'desc': request.data.get('desc'),
            'is_open': request.data.get('is_open'),
            'handle_by': int(request.data.get('handle_by')),
            'created_by': request.user.id,
            'updated_by': request.user.id,
        }
        serializer = BugSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            #log error
            pass
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
