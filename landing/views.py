from django.shortcuts import render
from .forms import SubscriberForm

from products.models import *



def landing(request):
    name = "CodingMedved"
    current_day = "03.01.2017"
    form = SubscriberForm(request.POST or None)
    if request.method =='POST' and form.is_valid():

        data = form.cleaned_data
        new_form = form.save()

    return render(request, 'landing.html', locals())

def home(request):
    products_images = ProductImage.objects.filter( is_main=True, product__category__id=2)
    products_images_second = ProductImage.objects.filter(product__category__id=1,is_main = True)
    #products_images_third = products_images.filter(product__category__id=2)
    return render(request, 'home.html', locals())
