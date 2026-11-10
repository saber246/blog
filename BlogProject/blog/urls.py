from django.contrib.auth import views as auth_views
from django.urls import path

from .views import favorites, index, index_detail, register, toggle_favorite

urlpatterns = [
    path('index/', index, name='index'),
    path('index/<int:pk>', index_detail, name='index_detail'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('<int:pk>/favorite/', toggle_favorite, name='toggle_favorite'),
    path('favorites/', favorites, name='favorites')
]
