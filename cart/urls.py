
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name='cart'
urlpatterns = [
    path('',views.product_list,	name='product_list'),
	path('<slug:category_slug>/',views.product_list,name='product_list_by_category'),
	path('<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
    
]
if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)