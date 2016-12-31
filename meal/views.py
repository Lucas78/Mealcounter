from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from dal import autocomplete
from .models import Meal, ItemMeal, Plate
from .forms import MealForm, ItemMealForm, PlateForm


@method_decorator(login_required, name='dispatch')
class MealList(ListView):
    paginate_by = 50
    model = Meal
    template_name = 'meal/list.html'


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

    def get_context_data(self, **kwargs):
        context = super(MealDetail, self).get_context_data(**kwargs)
        context['itemmeal'] = self.object.item_meal.all()
        return context


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
