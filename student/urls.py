from django.conf.urls import url
from . import views


urlpatterns = [
    # Student
    url(r'^student/list/$',
        views.StudentList.as_view(), name='student_list'),
    url(r'^student/add/$',
        views.StudentCreate.as_view(), name='student_add'),
    url(r'^student/details/(?P<pk>[0-9]+)/$',
        views.StudentDetail.as_view(), name='student_details'),
    url(r'^student/edit/(?P<pk>[0-9]+)/$',
        views.StudentUpdate.as_view(), name='student_edit'),
    url(r'^student/(?P<pk>[0-9]+)/delete/$',
        views.StudentDelete.as_view(), name='student_delete'),
    # Check
    url(r'^check/list/$',
        views.CheckList.as_view(), name='check_list'),
    url(r'^check/add/$',
        views.CheckCreate.as_view(), name='check_add'),
    url(r'^check/details/(?P<pk>[0-9]+)/$',
        views.CheckDetail.as_view(), name='check_details'),
    url(r'^check/edit/(?P<pk>[0-9]+)/$',
        views.CheckUpdate.as_view(), name='check_edit'),
    url(r'^check/(?P<pk>[0-9]+)/delete/$',
        views.CheckDelete.as_view(), name='check_delete'),
]
