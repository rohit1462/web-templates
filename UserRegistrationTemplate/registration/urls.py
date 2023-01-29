from django.urls import path
from registration import views


urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.check_login, name = 'login'),
    path('profile/',views.show_profile,name = 'profile'),
    path('logout/',views.show_logout,name ='logout'),
    path('changepass/',views.show_change_password,name = 'changepass'),
    path('resetpass/',views.show_reset_password,name = 'resetpass'),
    path('',views.show_home,name='home')
]
