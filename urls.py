from django.urls import path
from .import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index),
    path('reg',views.signup),
    path('log',views.signin),
    path('itemview',views.itemview),
    path('addtocart',views.addtocart),
    path('viewcart',views.viewcart),
    path('cart_del',views.cart_del),
    path('paydirect',views.paydirect),
    path('pay',views.pay),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)