from django.conf.urls import url
from . import views

urlpatterns = [
    url('',views.index,name='index'),
    url('user/',views.userPage,name='userPage'),
    url('product/',views.food,name='food'),
    url('register/',views.register,name='register'),
    url('login/',views.login,name='login'),
    url('logout/',views.logut,name='logout'),
    url('bmi/',views.bmi,name='bmi'),
    url('addfood/',views.addfood,name='addfood'),

]