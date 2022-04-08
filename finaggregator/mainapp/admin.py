from django.contrib import admin
from mainapp.models import Person, Client, Document, Bank, Service, ServiceCredit, PassportPerson
# Register your models here.
admin.site.register(Person)
admin.site.register(Client)
admin.site.register(Document)
admin.site.register(Bank)
admin.site.register(Service)
admin.site.register(ServiceCredit)
admin.site.register(PassportPerson)