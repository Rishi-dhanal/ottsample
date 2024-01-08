from django.contrib.admin import views
from django.urls import path

from .views import ott_home_view, register_user, login_user, membership, \
    select_user_type, adult_user_page, child_user_page

urlpatterns=[
    path('',ott_home_view,name='home_path'),
    path('user/',register_user,name='registration'),
    path('account/',login_user, name='login'),
    path('user/',membership, name='membership'),
    path('select-user-type/', select_user_type, name='select_user_type'),
    path('adult-page/', adult_user_page, name='adult_user_page'),
    path('child-page/', child_user_page, name='child_user_page'),
]