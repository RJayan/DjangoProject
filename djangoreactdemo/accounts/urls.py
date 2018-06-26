from django.urls import path,re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('inven/', views.inven, name='inven'), #  /inven/
    #path('inven/sample',views.sample,name='sample'), #
    #url(r'^$',views.inven,name="inven"),
    re_path(r'(?P<product_id>[0-9]+)/', views.sample, name = 'sample'),

    #url(r'^(?P<product_id>[0-9]+)/$', views.sample, name = 'sample'),
]
