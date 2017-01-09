# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from student.models import Student

# Página inicial


def index(request):
    if ('user' in request and
            Student.objects.filter(user_ptr=request.user).exists()):
        return HttpResponseRedirect('/meal/student/list/')

    return render(request, 'index.html')
