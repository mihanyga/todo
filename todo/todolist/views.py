from rest_framework.viewsets import ModelViewSet
from todolist.models import Project, Todo
from users.serializers import ProjectHyperlinkedModelSerializer, TodoHyperlinkedModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectHyperlinkedModelSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoHyperlinkedModelSerializer
