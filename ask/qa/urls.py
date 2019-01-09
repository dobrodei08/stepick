from django.conf.urls import url
from qa.views import test, newqwest, popqwest, oneqwest, askfr, signup, loginus

urlpatterns = [
    url(r'^login/.*$', loginus, name='login'),
    url(r'^signup/.*$', signup, name='sign'),
    url(r'^question/(?P<pk>\d+)/$', oneqwest, name='question'),
    url(r'^ask/.*$', askfr, name='askfr'),
    url(r'^popular/.*$', popqwest, name='pop-qwest'),
    url(r'^new/.*$', test, name='test'),
    url(r'^$', newqwest, name='new-qw')
    ]
