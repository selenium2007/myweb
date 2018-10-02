from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^require_login/$',views.require_login,name='require_login'),
    url(r'^login/$',views.login,name='login'),
    url(r'^login_success/$',views.login_success,name='login_success'),
    url(r'^require_register/$',views.require_register,name='require_register'),
    url(r'^register/$',views.register,name='register'),
    url(r'^register_success/$',views.register_success,name='register_success'),
    url(r'^under_construction/$',views.under_construction,name='under_construction'),
]
