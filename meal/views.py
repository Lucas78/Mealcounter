from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from dal import autocomplete
from .models import Meal, ItemMeal, Plate, Allergy
from .forms import MealForm, ItemMealForm, PlateForm, AllergyForm


@method_decorator(login_required, name='dispatch')
class MealList(ListView):
    paginate_by = 50
    model = Meal
    template_name = 'meal/list.html'


@method_decorator(login_required, name='dispatch')
class MealStudentList(ListView):
    paginate_by = 50
    model = Meal
    template_name = 'meal/student/list.html'

    def get_context_data(self, **kwargs):
        context = super(MealStudentList, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


@method_decorator(login_required, name='dispatch')
class MealCreate(CreateView):
    model = Meal
    template_name = 'meal/add.html'
    form_class = MealForm


@method_decorator(login_required, name='dispatch')
class MealUpdate(UpdateView):
    model = Meal
    template_name = 'meal/add.html'
    form_class = MealForm


@method_decorator(login_required, name='dispatch')
class MealDetail(DetailView):
    model = Meal
    template_name = 'meal/details.html'


@method_decorator(login_required, name='dispatch')
class MealDelete(DeleteView):
    model = Meal
    success_url = reverse_lazy('meal:meal_list')
    template_name = 'meal/delete.html'


# Autocomplete itemmeal

class ItemMealAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        qs = ItemMeal.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


@method_decorator(login_required, name='dispatch')
class ItemMealList(ListView):
    model = ItemMeal
    template_name = 'itemmeal/list.html'


@method_decorator(login_required, name='dispatch')
class ItemMealCreate(CreateView):
    model = ItemMeal
    template_name = 'itemmeal/add.html'
    form_class = ItemMealForm


@method_decorator(login_required, name='dispatch')
class ItemMealUpdate(UpdateView):
    model = ItemMeal
    template_name = 'itemmeal/add.html'
    form_class = ItemMealForm


@method_decorator(login_required, name='dispatch')
class ItemMealDetail(DetailView):
    model = ItemMeal
    template_name = 'itemmeal/details.html'


@method_decorator(login_required, name='dispatch')
class ItemMealDelete(DeleteView):
    model = ItemMeal
    success_url = reverse_lazy('meal:item_meal_list')
    template_name = 'itemmeal/delete.html'


# Autocomplete itemmeal

class PlateAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        qs = Plate.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


@method_decorator(login_required, name='dispatch')
class PlateList(ListView):
    paginate_by = 60
    model = Plate
    template_name = 'plate/list.html'


@method_decorator(login_required, name='dispatch')
class PlateCreate(CreateView):
    model = Plate
    template_name = 'plate/add.html'
    form_class = PlateForm


@method_decorator(login_required, name='dispatch')
class PlateUpdate(UpdateView):
    model = Plate
    template_name = 'plate/add.html'
    form_class = PlateForm


@method_decorator(login_required, name='dispatch')
class PlateDetail(DetailView):
    model = Plate
    template_name = 'plate/details.html'


@method_decorator(login_required, name='dispatch')
class PlateDelete(DeleteView):
    model = Plate
    success_url = reverse_lazy('meal:plate_list')
    template_name = 'plate/delete.html'


# Autocomplete itemmeal

class AllergyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        qs = Allergy.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


@method_decorator(login_required, name='dispatch')
class AllergyList(ListView):
    model = Allergy
    template_name = 'allergy/list.html'


@method_decorator(login_required, name='dispatch')
class AllergyCreate(CreateView):
    model = Allergy
    template_name = 'itemmeal/add.html'
    form_class = AllergyForm


@method_decorator(login_required, name='dispatch')
class AllergyUpdate(UpdateView):
    model = Allergy
    template_name = 'allergy/add.html'
    form_class = AllergyForm


@method_decorator(login_required, name='dispatch')
class AllergyDetail(DetailView):
    model = Allergy
    template_name = 'allergy/details.html'


@method_decorator(login_required, name='dispatch')
class AllergyDelete(DeleteView):
    model = Allergy
    success_url = reverse_lazy('meal:allergy_list')
    template_name = 'allergy/delete.html'
