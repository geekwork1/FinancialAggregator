from django.shortcuts import render

# Create your views here.

def main(reqest):
    return render(reqest, 'mainapp/index.html')

def product(reqest):
    return render(reqest, 'mainapp/products.html')

def contact(reqest):
    return render(reqest, 'mainapp/contacts.html')
