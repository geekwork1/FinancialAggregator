from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from userprofileapp.models import UserProfile
from usersapp.models import User
from userprofileapp.serializers import UserSerializer, UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):

    http_method_names = ['get', 'patch']
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        self.queryset = UserProfile.objects.all().filter(pk=self.request.user.id)
        return self.queryset

    serializer_class = UserProfileSerializer

