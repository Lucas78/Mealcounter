from django.conf.urls import url
from .views import index

urlpatterns = [
    # Index
    url(r'^$', index, name='index'),
]
