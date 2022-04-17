from rest_framework import serializers
from mainapp.models import PassportPerson, Person, Client, ClientFinanceHistory, Document, Bank, Service, \
    ServiceCredit, Snippet
from django.contrib.auth.models import User

"""
    https://www.django-rest-framework.org/tutorial/1-serialization/
"""


# class SnippetSerializerHighlight(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name="mainapp")
#     owner = serializers.ReadOnlyField(source='owner.username')
#     highlight = serializers.HyperlinkedIdentityField(
#         view_name='snippet-highlight', format='html')
#
#     class Meta:
#         model = Snippet
#         fields = ('url', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')



class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlighted']


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PassportPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportPerson
        fields = '__all__'

    owner = serializers.ReadOnlyField(source='owner.username')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientFinanceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientFinanceHistory
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCredit
        fields = '__all__'
