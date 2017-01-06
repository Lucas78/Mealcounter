from django.conf.urls import url
from . import views

urlpatterns = [
    # Autocomplete
    url(r'^item-meal-autocomplete/$',
        views.ItemMealAutocomplete.as_view(), name='item_meal_autocomplete'),
    url(r'^plate-autocomplete/$',
        views.PlateAutocomplete.as_view(), name='plate_autocomplete'),
    url(r'^allergy-autocomplete/$',
        views.AllergyAutocomplete.as_view(), name='allergy_autocomplete'),
    # Meal
    url(r'^meal/list/$', views.MealList.as_view(), name='meal_list'),
    url(r'^meal/student/list/$',
        views.MealStudentList.as_view(), name='meal_student_list'),
    url(r'^meal/add/$', views.MealCreate.as_view(), name='meal_add'),
    url(r'^meal/details/(?P<pk>[0-9]+)/$',
        views.MealDetail.as_view(), name='meal_details'),
    url(r'^meal/edit/(?P<pk>[0-9]+)/$',
        views.MealUpdate.as_view(), name='meal_edit'),
    url(r'^meal/(?P<pk>[0-9]+)/delete/$',
        views.MealDelete.as_view(), name='meal_delete'),
    # ItemMeal
    url(r'^itemmeal/list/$',
        views.ItemMealList.as_view(), name='item_meal_list'),
    url(r'^itemmeal/add/$',
        views.ItemMealCreate.as_view(), name='item_meal_add'),
    url(r'^itemmeal/details/(?P<pk>[0-9]+)/$',
        views.ItemMealDetail.as_view(), name='item_meal_details'),
    url(r'^itemmeal/edit/(?P<pk>[0-9]+)/$',
        views.ItemMealUpdate.as_view(), name='item_meal_edit'),
    url(r'^itemmeal/(?P<pk>[0-9]+)/delete/$',
        views.ItemMealDelete.as_view(), name='item_meal_delete'),
    # Plate
    url(r'^plate/list/$', views.PlateList.as_view(), name='plate_list'),
    url(r'^plate/add/$', views.PlateCreate.as_view(), name='plate_add'),
    url(r'^plate/details/(?P<pk>[0-9]+)/$',
        views.PlateDetail.as_view(), name='plate_details'),
    url(r'^plate/edit/(?P<pk>[0-9]+)/$',
        views.PlateUpdate.as_view(), name='plate_edit'),
    url(r'^plate/(?P<pk>[0-9]+)/delete/$',
        views.PlateDelete.as_view(), name='plate_delete'),
    # Allergy
    url(r'^allergy/list/$', views.AllergyList.as_view(), name='allergy_list'),
    url(r'^allergy/add/$', views.AllergyCreate.as_view(), name='allergy_add'),
    url(r'^allergy/details/(?P<pk>[0-9]+)/$',
        views.AllergyDetail.as_view(), name='allergy_details'),
    url(r'^allergy/edit/(?P<pk>[0-9]+)/$',
        views.AllergyUpdate.as_view(), name='allergy_edit'),
    url(r'^allergy/(?P<pk>[0-9]+)/delete/$',
        views.AllergyDelete.as_view(), name='allergy_delete'),
]
