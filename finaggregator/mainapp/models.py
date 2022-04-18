from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from django.conf import settings
from django.utils import timezone

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class ParentModel(models.Model):
    class Meta:
        abstract = True
        ordering = ['created']

    created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField(blank=True)
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='Python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                              related_name="%(app_label)s_%(class)s_related",
                              related_query_name="%(app_label)s_%(class)ss")
    highlighted = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language, stripall=True)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, cssclass='OutDataHTML', **options)
        text = ''
        for key, value in self.__dict__.items():
            text += str(key) + ' : ' + str(value) + '\n'
        self.highlighted = highlight(text, lexer, formatter)
        super().save(*args, **kwargs)


class Snippet(ParentModel):
    pass


class PassportPerson(ParentModel):
    number = models.CharField(verbose_name='Номер паспорта', max_length=20, unique=True, null=True,
                              blank=True, default='Не заполнено')
    date = models.DateTimeField(verbose_name='Дата получения', null=True, blank=True)
    scan_document = models.ImageField(upload_to='document', verbose_name='Паспорта скан', blank=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.number}, получен: {self.date}, обновлено: {self.updated}'


class Person(ParentModel):
    inn = models.CharField(unique=True, max_length=50, verbose_name='индивидуальный ИНН гр-на', default='')
    name = models.CharField(max_length=200, verbose_name="Имя", default='')
    last_name = models.CharField(max_length=200, verbose_name="Отчество", default='')
    sur_name = models.CharField(max_length=200, verbose_name="Фамилия", default='')
    telephone = models.CharField(max_length=12, verbose_name='Номер телефона', default='', blank=True)
    email = models.CharField(max_length=50, verbose_name='Почтовый ящик', default='', blank=True)
    registration_city = models.CharField(max_length=50, verbose_name='Город регистрации гр-на', default='', blank=True)
    registration_region = models.CharField(max_length=50, verbose_name='Регион регистрации гр-на', default='',
                                           blank=True)
    registration_street = models.CharField(max_length=50, verbose_name='Улица регистрации гр-на', default='',
                                           blank=True)
    registration_building = models.CharField(max_length=50, verbose_name='Здание регистрации гр-на', default='',
                                             blank=True)
    registration_room = models.CharField(max_length=50, verbose_name='Помещение регистрации гр-на', default='',
                                         blank=True)
    documents = models.ForeignKey(PassportPerson, on_delete=models.CASCADE,
                                  verbose_name='Паспортные данные', null=True, blank=True,
                                  related_name="%(app_label)s_%(class)s_related",
                                  related_query_name="%(app_label)s_%(class)ss")
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.name} {self.last_name} {self.sur_name}'


class Client(ParentModel):
    inn = models.CharField(unique=True, max_length=50, verbose_name='ИНН клиента', default='')
    organization_type = models.CharField(max_length=50, verbose_name='Тип организации', default='')
    title = models.CharField(max_length=50, verbose_name='Название клиента', default='')
    task = models.TextField(max_length=300, verbose_name='Описание клиента', default='', blank=True)
    director = models.ForeignKey(Person, on_delete=models.SET_DEFAULT, default='',
                                 verbose_name='Директор', related_name='client_person_set')
    telephone = models.CharField(max_length=12, verbose_name='Номер телефона организации', default='', blank=True)
    email = models.CharField(max_length=50, verbose_name='Почтовый ящик организации', default='', blank=True)
    site = models.CharField(max_length=50, verbose_name='Сайт организации', default='', blank=True)
    registration_city = models.CharField(max_length=50, verbose_name='Город регистрации организации', default='',
                                         blank=True)
    registration_region = models.CharField(max_length=50, verbose_name='Регион регистрации организации', default='',
                                           blank=True)
    registration_street = models.CharField(max_length=50, verbose_name='Улица регистрации организации', default='',
                                           blank=True)
    registration_building = models.CharField(max_length=50, verbose_name='Здание регистрации организации', default='',
                                             blank=True)
    registration_room = models.CharField(max_length=50, verbose_name='Помещение регистрации организации', default='',
                                         blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Название: {self.title}  ИНН: {self.inn}'


class ClientFinanceHistory(ParentModel):
    name = models.CharField(max_length=100, default='', verbose_name='Выручка клиента')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Document(ParentModel):
    name = models.CharField(max_length=100, default='', verbose_name='Сканы документов клиента')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order = models.ImageField(upload_to='document', verbose_name='Решение', blank=True)
    decree = models.ImageField(upload_to='document', verbose_name='Устав', blank=True)
    lease_contract = models.ImageField(upload_to='document', verbose_name='Договор аренды', blank=True)
    document = models.ImageField(upload_to='document', verbose_name='Свидетельство', blank=True)
    declaration_one = models.ImageField(upload_to='document', verbose_name='Декларация за предыдущий 1-ый год',
                                        blank=True)
    declaration_two = models.ImageField(upload_to='document', verbose_name='Декларация за предыдущий 2-ый год',
                                        blank=True)
    declaration_three = models.ImageField(upload_to='document', verbose_name='Декларация за предыдущий 3-ый год',
                                          blank=True)
    balance_one = models.ImageField(upload_to='document', verbose_name='Баланс за предыдущий 1-ый год', blank=True)
    balance_two = models.ImageField(upload_to='document', verbose_name='Баланс за предыдущий 2-ый год', blank=True)
    balance_three = models.ImageField(upload_to='document', verbose_name='Баланс за предыдущий 3-ый год', blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Bank(ParentModel):
    name = models.CharField(max_length=100, default='', verbose_name='Название банка')
    task = models.TextField(max_length=300, verbose_name='Описание банка', default='', blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Service(ParentModel):
    name = models.CharField(max_length=100, default='', verbose_name='Название услуги')
    task = models.TextField(max_length=300, verbose_name='Описание услуги', default='', blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ServiceCredit(ParentModel):
    name = models.CharField(max_length=100, default='', verbose_name='Заказ кредита')
    task = models.TextField(max_length=300, verbose_name='Описание кредита', default='', blank=True)
    client = models.ForeignKey(Client, on_delete=models.SET_DEFAULT, default='Данные по клиенту отсутствуют',
                               verbose_name='Клиент по услуге')
    total = models.CharField(max_length=12, default='0', validators=[validate_comma_separated_integer_list])
    deposit = models.BooleanField(verbose_name='Наличие залога', default=False)
    credit_term = models.PositiveSmallIntegerField("year", choices=settings.NUMBER_OF_YEARS, default=1)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
