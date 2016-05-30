from django.conf.urls import url
from . import views
from .forms import LoginForm
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', login, name='login', kwargs={
        'template_name': 'accounts/login_form.html',
        'authentication_form': LoginForm,
    }),
    url(r'^logout/$', logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
]
