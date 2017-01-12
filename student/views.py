from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from meal.models import Meal, Plate, ItemMeal
from .models import Student, Check
from .forms import StudentForm, StudentUpdateForm, CheckForm


@method_decorator(login_required, name='dispatch')
class StudentList(ListView):

    paginate_by = 50
    model = Student
    template_name = 'student/list.html'


@method_decorator(login_required, name='dispatch')
class StudentCreate(CreateView):

    model = Student
    template_name = 'student/add.html'
    form_class = StudentForm


@method_decorator(login_required, name='dispatch')
class StudentUpdate(UpdateView):

    model = Student
    template_name = 'student/add.html'
    form_class = StudentUpdateForm


@method_decorator(login_required, name='dispatch')
class StudentDetail(DetailView):

    model = Student
    template_name = 'student/details.html'


@method_decorator(login_required, name='dispatch')
class StudentDelete(DeleteView):

    model = Student
    success_url = reverse_lazy('student:student_list')
    template_name = 'student/delete.html'


@method_decorator(login_required, name='dispatch')
class CheckList(ListView):

    paginate_by = 50
    model = Check
    template_name = 'check/list.html'


@login_required
def check_list(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except:
        raise Http404('Estudante não existe')

    dangerous_items = ItemMeal.objects.filter(
        allergy__in=student.allergy.values_list('pk'))
    dangerous_plates = []
    if dangerous_items:
        dangerous_plates = Plate.objects.filter(
            item_meal__in=dangerous_items.values_list('pk'))

    if request.method == 'GET':
        checks = Check.objects.filter(student=student)
        context = {
            'object_list': checks,
            'aluno': student,
            'dangerous_items': dangerous_items,
            'dangerous_plates': dangerous_plates
        }
        return render(
            request, 'check/admin/list.html', context)
    return HttpResponseNotFound("Página não encontrada")


@login_required
def check_in(request, pk):
    error = ''
    try:
        student = Student.objects.get(user_ptr=request.user)
        meal = Meal.objects.get(pk=pk)
    except:
        raise Http404('Refeição não existe')

    try:
        check = Check.objects.get(meal=meal, student=student)
    except:
        check = None

    if request.method == 'POST':
        if 'plate' in request.POST and request.POST['plate']:
            plate = Plate.objects.get(pk=request.POST['plate'])
            if check:
                check.plate = plate
            else:
                check = Check(student=student, meal=meal, plate=plate)
            check.save()
            return HttpResponseRedirect('/meal/student/list/')
        else:
            error = 'Por favor, selecione um prato.'
    context = {
        'meal': meal,
        'check': check,
        'error': error
    }
    return render(request, 'check/add.html', context)


@method_decorator(login_required, name='dispatch')
class CheckDetail(DetailView):

    model = Check
    template_name = 'check/details.html'


@method_decorator(login_required, name='dispatch')
class CheckDelete(DeleteView):

    model = Check
    success_url = reverse_lazy('student:check_list')
    template_name = 'check/delete.html'
