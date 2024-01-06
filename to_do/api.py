from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['Get'])
def task_list_api (request):
    all_tasks = Task.objects.all()
    data = TaskSerializer(all_tasks,many=True).data
    
    return Response({'data':data})

@api_view(['Get'])
def task_detail_api(request,pk):
    task = Task.objects.get(id = pk)
    data = TaskSerializer(task).data
    
    return Response({'data':data})

class TasksCreateApi(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'