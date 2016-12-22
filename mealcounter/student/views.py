from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from dal import autocomplete
from django.db.models import Sum
from django.db.models.functions import Coalesce
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

method_decorator(login_required, name='dispatch')
class StudentList(ListView):
	
	paginate_by = 50
	model = Student
	template_name = 'adc_student/list.html'

@method_decorator(login_required, name='dispatch')
class StudentCreate(CreateView):

	model = Student 
	template_name = 'adc_student/add.html'
	form_class = StudentForm

@method_decorator(login_required, name='dispatch')
class StudentUpdate(UpdateView):

	model = Student
	template_name = 'adc_student/add.html'
	form_class = StudentForm

@method_decorator(login_required, name='dispatch')
class StudentDetail(DetailView):

	model = Student
	template_name = 'adc_student/details.html'

	def get_context_data(self, **kwargs):
		context = super(Detail,self).get_context_data(**kwargs)
		context['adc_student']=self.object.adc_student.all() 
		return context

@method_decorator(login_required, name='dispatch')
class StudentDelete(DeleteView):

	model = Student
	success_url = reverse_lazy('adc_student:student_list')
	template_name = 'adc_student/delete.html'