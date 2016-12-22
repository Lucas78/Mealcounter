from django.conf.urls import include, url
from django.contrib import admin
from .views import*

ulpatterns [
	# Student
	url(r'^adc_student/list/$', StudentList.as_view(), name='adc_student_list'),
    url(r'^adc_student/add/$', StudentCreate.as_view(), name='adc_student_add'),
	url(r'^adc_student/details/(?P<pk>[0-9]+)/$', StudentDetail.as_view(), name='adc_student_details'),
	url(r'^adc_student/edit/(?P<pk>[0-9]+)/$', StudentUpdate.as_view(), name='adc_student_edit'),
	url(r'^adc_student/(?P<pk>[0-9]+)/delete/$', StudentDelete.as_view(), name='adc_student_delete'), 

]