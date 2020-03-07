from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.login),   
        url(r'^main$', views.main),
        url(r'^log_in$', views.log_in),  
        url(r'^new_restaurant$', views.new_restaurant),
        url(r'^create_restaurant$', views.create_restaurant),
        url(r'^update_restaurant/(?P<id>[0-9]+)$', views.update_restaurant),
        url(r'^edit_restaurant/(?P<id>[0-9]+)$', views.edit_restaurant),
        url(r'^delete_restaurant/(?P<id>[0-9]+)$', views.delete_restaurant),
        url(r'^new_product$', views.new_product),
        url(r'^create_product$', views.create_product),
        url(r'^update_product/(?P<id>[0-9]+)$', views.update_product),
        url(r'^edit_product/(?P<id>[0-9]+)$', views.edit_product),
        url(r'^delete_product/(?P<id>[0-9]+)$', views.delete_product),
        url(r'^today_order$', views.today_order),
]