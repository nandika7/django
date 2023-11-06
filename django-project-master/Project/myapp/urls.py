from django.urls import path

from .views import home, predict_diabetes, register, login, logout, update_health_details, about_us, find_doctors

urlpatterns=[
    path('', home, name="home"),
    path('about_us/', about_us, name = "about_us"),
    path('predict_diabetes/', predict_diabetes, name="predict_diabetes"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout, name='logout'),
    path('update_health_details', update_health_details, name = 'update_health_details'),
    path('find_doctors', find_doctors, name = 'find_doctors')

]
#google.com/id=2&name=abc