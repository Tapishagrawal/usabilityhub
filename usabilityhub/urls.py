from django.contrib import admin
from django.urls import path
from usabilityhub import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('overview/',views.overview,name='overview'),
    path('card-sorting/',views.card_sorting,name='card-sorting'),
    path('prototype/',views.prototype,name='prototype'),
    path('design-surveys/',views.design_surveys,name='design-surveys'),
    path('five-second/',views.five_second,name='five-second'),
    path('preference/',views.preference,name='preference'),
    path('first-click-test/',views.first_click,name='first-click-test'),
    path('panel/',views.panel,name='panel'),
    path('customer/',views.customer,name='customer'),
    path('pricing/',views.pricing,name='pricing'),
    path('guides/',views.guides,name='guides'),
]
