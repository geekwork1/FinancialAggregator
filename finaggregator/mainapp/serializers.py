from rest_framework import serializers
from mainapp.models import PassportPerson, Person, Client, ClientFinanceHistory, Document, Bank, Service, \
    ServiceCredit, Snippet
from django.contrib.auth.models import User

"""
    https://www.django-rest-framework.org/tutorial/1-serialization/
"""


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'owner']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'inn', 'name', 'last_name', 'sur_name', 'telephone', 'email', 'registration_city',
            'registration_region', 'registration_building', 'registration_room', 'documents',
            'updated',
        ]


class PassportPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportPerson
        fields = [
            'number', 'date', 'scan_document', 'updated', 'owner'
        ]

    owner = serializers.ReadOnlyField(source='owner.username')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'inn', 'organization_type', 'title', 'task', 'director', 'telephone',
            'email', 'site', 'registration_city', 'registration_region',
            'registration_street', 'registration_building', 'registration_room', 'updated', 'owner'
        ]


class ClientFinanceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientFinanceHistory
        fields = [
            'name', 'client', 'updated', 'owner'
        ]


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            'name','client', 'order', 'decree', 'lease_contract', 'document',
            'declaration_one', 'declaration_two', 'declaration_three', 'balance_one',
            'balance_two', 'balance_three', 'updated', 'owner'
        ]


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = [
            'name', 'task', 'client', 'updated', 'owner'
        ]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'name', 'task', 'updated', 'owner'
        ]


class ServiceCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCredit
        fields = [
            'name', 'task', 'client', 'total', 'deposit', 'credit_term', 'updated', 'owner'
        ]
