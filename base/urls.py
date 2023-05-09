from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.home, name="home"),
    path('room/<str:pk>/',views.room, name='room' ),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),

    path('create_room/', views.createRoom, name="create-room"),
    path('update_room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete_room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete_message/<str:pk>/', views.deleteMessage, name="delete-message"),

    path('shop/', views.shop, name="shop"),
    path('shop/game/<str:pk>/', views.product, name="product"),

    path('about/', views.about, name='about'),
    path('useful_links/', views.useful_links, name='links'),

    path('pool/', views.pool, name='pool'),
    path('answered_pool/<str:pk>/', views.answered_pool, name='answered_pool'),

    path('video/', views.video, name='video'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
