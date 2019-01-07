from django.conf.urls import url
from qa.views import test, newqwest, popqwest, oneqwest

urlpatterns = [
    url(r'^login/.*$', test, name='test'),
    url(r'^signup/.*$', test, name='test'),
    url(r'^question/(?P<pk>\d+)/$', oneqwest, name='question'),
    url(r'^ask/.*$', test, name='test'),
    url(r'^popular/.*$', popqwest, name='pop-qwest'),
    url(r'^new/.*$', test, name='test'),
    url(r'^$', newqwest, name='new-qw')
    ]
