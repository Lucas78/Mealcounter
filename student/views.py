from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from .models import Student, Check
from .forms import StudentForm, CheckForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
    form_class = StudentForm


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


@method_decorator(login_required, name='dispatch')
class CheckCreate(CreateView):

    model = Check
    template_name = 'check/add.html'
    form_class = CheckForm


@method_decorator(login_required, name='dispatch')
class CheckUpdate(UpdateView):

    model = Check
    template_name = 'check/add.html'
    form_class = CheckForm


@method_decorator(login_required, name='dispatch')
class CheckDetail(DetailView):

    model = Check
    template_name = 'check/details.html'


@method_decorator(login_required, name='dispatch')
class CheckDelete(DeleteView):

    model = Check
    success_url = reverse_lazy('student:check_list')
    template_name = 'check/delete.html'
