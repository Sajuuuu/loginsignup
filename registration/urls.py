from django.urls import path
from. import views
urlpatterns = [ 
    path('',views.signuppage,name='signup'),
    path('login',views.loginpage,name='login'),
    path('home',views.homepage,name='home'),
    path('library',views.library,name='library'),
    path('logout',views.logoutpage,name='logout'),
   
]