from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserHyperlinkedModelSerializer
from djangorestframework_camel_case.render import CamelCaseBrowsableAPIRenderer


class UserModelViewSet(ModelViewSet):    
    renderer_classes = [CamelCaseBrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserHyperlinkedModelSerializer



