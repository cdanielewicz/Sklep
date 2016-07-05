from django.shortcuts import render

from django.http import HttpResponse

from sklep.models import Product

# Create your views here.
def index(request):
    produkty = Product.objects.all()
    return render(request,
                  "sklep/o-nas.html",
                  {"produkty":produkty})

def products(request):
    produkty = Product.objects.all()
    return render(request,
                  "sklep/produkty.html",
                  {"products": produkty})
    # return HttpResponse ("Hello World")