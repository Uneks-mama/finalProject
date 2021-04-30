from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('/profile/', views.profile_list, name='profile'),
    path('/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('/contactus/', views.contact_us, name='contactus'),
    # path('/redirect/', views.redirect_view)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
