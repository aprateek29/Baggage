from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('coming/', views.coming_view, name='coming'),
    path('shop/', views.shop_view, name='shop'),
    path('shop/<int:id>/', views.shop_single_view, name='shop-single'),
    path('newsletter/', views.newsletter, name='newsletter'),
]