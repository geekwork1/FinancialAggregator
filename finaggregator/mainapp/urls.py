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
from django.urls import path
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static

from mainapp import views

urlpatterns = [
    path('', mainapp.main),
    path('contact/', mainapp.contact, name='contact'),
    path('product/', mainapp.product, name='product'),
    path('pasport/', views.PassportPersonList.as_view(), name='person_list'),
    path('passport/<int:pk>/', views.PassportPersonDetail.as_view()),
    path('person/', views.PersonList.as_view(), name='person_list'),
    path('person/<int:pk>/', views.PersonDetail.as_view()),
    path('client/', views.ClientList.as_view(), name='person_list'),
    path('client/<int:pk>/', views.ClientDetail.as_view()),
    path('clients_finance_history/', views.ClientFinanceHistoryList.as_view(), name='person_list'),
    path('clients_finance_history/<int:pk>/', views.ClientFinanceHistoryDetail.as_view()),
    path('document/', views.DocumentList.as_view(), name='person_list'),
    path('document/<int:pk>/', views.DocumentDetail.as_view()),
    path('bank/', views.BankList.as_view(), name='person_list'),
    path('bank/<int:pk>/', views.BankDetail.as_view()),
    path('serviece/', views.ServiceList.as_view(), name='person_list'),
    path('service/<int:pk>/', views.ServiceDetail.as_view()),
    path('serviececredit/', views.ServiceCreditList.as_view(), name='person_list'),
    path('servicecredit/<int:pk>/', views.ServiceCreditDetail.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)