from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework import permissions, renderers, filters
from mainapp.models import Person, Client, PassportPerson, Service, ServiceCredit, Bank, Document, \
    ClientFinanceHistory, Snippet
from mainapp.permmissions import IsOwnerOrReadOnly
from mainapp.serializers import PersonSerializer, ClientSerializer, PassportPersonSerializer, ServiceSerializer, \
    ServiceCreditSerializer, BankSerializer, DocumentSerializer, ClientFinanceHistorySerializer, \
    UserSerializer, SnippetSerializer
from django.contrib.auth.models import User

# Create your views here.
"""
https://www.django-rest-framework.org/tutorial/1-serialization/
"""

class ListPagination(PageNumberPagination):
    page_size = 5


class ParentModelViewSet(ModelViewSet):
    class Meta:
        abstract = True

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = ListPagination
    filter_backends = (filters.SearchFilter,)
    # search_fields = ('',)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        print(f'self.request.user:  {self.request.__dict__}')
        # serializer.save(owner=self.request)

        serializer.save()


class SnippetDetail(ParentModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    search_fields = ('title', 'id')
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserDetail(ReadOnlyModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PassportPersonDetail(ParentModelViewSet):
    queryset = PassportPerson.objects.all()
    serializer_class = PassportPersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class PersonDetail(ParentModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ClientDetail(ParentModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientFinanceHistoryDetail(ParentModelViewSet):
    queryset = ClientFinanceHistory.objects.all()
    serializer_class = ClientFinanceHistorySerializer


class DocumentDetail(ParentModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class BankDetail(ParentModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class ServiceDetail(ParentModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceCreditDetail(ParentModelViewSet):
    queryset = ServiceCredit.objects.all()
    serializer_class = ServiceCreditSerializer


def main(request):
    return render(request, 'mainapp/index.html')


def product(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contacts.html')
