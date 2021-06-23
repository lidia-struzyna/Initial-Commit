from django.urls import path
#from userProfile import views
#from userProfile.views import login, register

urlpatterns = [
    path('', views.profile, name='login_page'),
]
