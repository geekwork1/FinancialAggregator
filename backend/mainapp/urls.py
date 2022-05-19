"""finaggregator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from mainapp.views import BankDetail, ClientDetail, ClientFinanceHistoryDetail, ServiceCreditDetail, DocumentDetail, \
    PassportPersonDetail, ServiceDetail, PersonDetail, UserDetail, SnippetDetail

app_name = "mainapp"
router = DefaultRouter()

router.register('passport', PassportPersonDetail, basename='passport')
router.register('person', PersonDetail, basename='person')
router.register('client', ClientDetail, basename='client')
router.register('clients_finance_history', ClientFinanceHistoryDetail, basename='clients_finance_history')
router.register('document', DocumentDetail, basename='document')
router.register('bank', BankDetail, basename='bank')
router.register('service', ServiceDetail, basename='service')
router.register('service-credit', ServiceCreditDetail, basename='service-credit')
router.register('user', UserDetail, basename='user')
router.register('snippet', SnippetDetail, basename='snippet')





urlpatterns = [

    path('', include(router.urls)),



]
urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
