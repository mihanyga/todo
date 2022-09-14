from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User
from todolist.models import Project, Todo


class UserHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProjectHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
     
class TodoHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'      
