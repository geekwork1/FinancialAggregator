from django.shortcuts import render
from rest_framework import generics
from mainapp.models import Person, Client, PassportPerson, Service, ServiceCredit, Bank, Document, ClientFinanceHistory
from mainapp.serializers import PersonSerializer, ClientSerializer, PassportPersonSerializer, ServiceSerializer, \
    ServiceCreditSerializer, BankSerializer, DocumentSerializer, ClientFinanceHistorySerializer

# Create your views here.
"""
https://www.django-rest-framework.org/tutorial/1-serialization/
"""

class PassportPersonList(generics.ListCreateAPIView):
    queryset = PassportPerson.objects.all()
    serializer_class = PassportPersonSerializer


class PassportPersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PassportPerson.objects.all()
    serializer_class = PassportPersonSerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientFinanceHistoryList(generics.ListCreateAPIView):
    queryset = ClientFinanceHistory.objects.all()
    serializer_class = ClientFinanceHistorySerializer


class ClientFinanceHistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientFinanceHistory.objects.all()
    serializer_class = ClientFinanceHistorySerializer


class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class BankList(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceCreditList(generics.ListCreateAPIView):
    queryset = ServiceCredit.objects.all()
    serializer_class = ServiceCreditSerializer


class ServiceCreditDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceCredit.objects.all()
    serializer_class = ServiceCreditSerializer




def main(reqest):
    return render(reqest, 'mainapp/index.html')


def product(reqest):
    return render(reqest, 'mainapp/products.html')


def contact(reqest):
    return render(reqest, 'mainapp/contacts.html')
