from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, renderers
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


class SnippetDetail(ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserDetail(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class SnippetDetail(ModelViewSet):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


class PassportPersonDetail(ModelViewSet):
    queryset = PassportPerson.objects.all()
    serializer_class = PassportPersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PersonDetail(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ClientDetail(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientFinanceHistoryDetail(ModelViewSet):
    queryset = ClientFinanceHistory.objects.all()
    serializer_class = ClientFinanceHistorySerializer


class DocumentDetail(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class BankDetail(ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class ServiceDetail(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceCreditDetail(ModelViewSet):
    queryset = ServiceCredit.objects.all()
    serializer_class = ServiceCreditSerializer


def main(request):
    return render(request, 'mainapp/index.html')


def product(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contacts.html')
