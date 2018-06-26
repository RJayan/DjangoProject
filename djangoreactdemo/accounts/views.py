from django.shortcuts import render
from django.http import HttpResponse
#from django.views.generic import TemplateView # Import TemplateView
from .models import Products

# def inven(request):
#     all_pro = Products.objects.all()
#     html = ''
#     for product in all_pro:
#         # url = '/inven/'+ productname +'/'
#         html+= '<a href="'+ url +'">' + product.product_name + '</a><br>'
#     return HttpResponse(html)    


# Create your views here.
def inven(request):
     all_products = Products.objects.all()
     for pro in all_products:
             url = '/inven' + str(pro.id) + '/'
             html = '<a href = " '+ url +'">' + pro.product_name + '</a><br>'
     return HttpResponse(html)
    #return HttpResponse("<h2>this is list of products </h2>")


def sample(request,product_id):
    return HttpResponse("<h2> Details for Product id:" + str(product_id) + "</h2>")
# class inven(TemplateView):
# 	template_name = "inventory.html"
    

# class sample(TemplateView):
#     template_name = "sample.html"
