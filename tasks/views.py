from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from .models import Task
from .serializers import TaskSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_tasks(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        tasks = Task.objects.filter(user_id=request.user.id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def tasks_detail(request, task_id):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = TaskSerializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method == "DELETE":
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def toggle_Status(status: str):
    TASK_STATUS_CHOICES = [
        'ready',
        'in_progress',
        'completed'
    ]
    status_index = TASK_STATUS_CHOICES.index(status) + 1
    if (status_index == 3):
        status_index = 0
    return TASK_STATUS_CHOICES[status_index]


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def task_status_toggle(request, task_id):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")

    task = get_object_or_404(Task, id=task_id)

    if request.method == "PUT":  # toggle is_Cooked
        task_status = {'status': toggle_Status(task.status)}
        serializer = TaskSerializer(
            task, data=task_status, partial=True)  # type: ignore
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
