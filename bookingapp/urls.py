from django.urls import path
from .views import UserAPI,getUpdateDeleteUser,UserSignupAPI,UserSigin,ContactAPI,getUpdateContact
from django.shortcuts import render
from django.conf.urls import url


urlpatterns = [
	#url(r'^home', views.index, name='index

    url(r'^api/users', UserAPI.as_view()),
    url(r'^api/user/(?P<id>[0-9]+)$',getUpdateDeleteUser.as_view()),
    url(r'^api/signup',UserSignupAPI.as_view()),
    url(r'^api/signin',UserSigin.as_view()),

    url(r'^api/contact', ContactAPI.as_view()),
    url(r'^api/contacts/(?P<id>[0-9]+)$',getUpdateContact.as_view()),
]
