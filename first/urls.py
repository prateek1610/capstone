from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name='welcome'),
    url(r'^about/$',views.about,name='about'),
    url(r'^updatemenu/$',views.menu_entry,name='mess_update'),
    url(r'^viewmenu/$',views.viewmenu,name='view_menu')
]