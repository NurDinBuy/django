from django.shortcuts import render, HttpResponse
from .models import Production, Category


# Create your views here.
def category(request):
    named = Category.objects.all()
    context = {'all_category': named}
    return render(request, 'category.html', context)


def show_products(request):
    product_object = Production.objects.get(id=1)
    description = product_object.description
    return HttpResponse(description)


def homepage(request):
    return HttpResponse('HOME PAGE')