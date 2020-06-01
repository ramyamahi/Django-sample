from django.conf.urls import  include, url
from myapp.views import hello, get_data, template_example, get_json_data

urlpatterns = [
    url(r'^hello/', hello, name = 'hello'),
    url(r'^getData/(\d+)', get_data, name = 'get_data'),
    url(r'^templateExample/', template_example, name = 'template_example'),
    url(r'^getJsonData/', get_json_data, name = 'get_json_data'),
]