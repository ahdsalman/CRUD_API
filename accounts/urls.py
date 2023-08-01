from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.UserRegisterationView.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('profile/',views.UserProfileView.as_view(),name='profile'),
    # path('proupdate/<int:pk>/',views.UserProfileView.as_view(),name='proupdate'),
    path('home/',views.HomePageView.as_view(),name='home'),
    # path('list/',views.ListPageView.as_view(),name='list'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),   
    path('block/<int:id>/',views.BlockAPIView.as_view(),name='block'), 
]