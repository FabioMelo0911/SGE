from django.urls import path
from . import views

# Definindo as rotas para a app brands
urlpatterns = [
    path('brands/list/', views.BrandListView.as_view(), name='brand_list'),

]

