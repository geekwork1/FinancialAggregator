# from rest_framework import viewsets
#
# from .models import User2
# from .serializers import User2Serializer
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     def get_queryset(self):
#         self.queryset = User2.objects.all().filter(user_id=self.request.user.id)
#         return self.queryset
#
#     serializer_class = User2Serializer
#     http_method_names = ['get', 'head']
