# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from models import Question, Answer
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from forms import AskForm, AnswerForm, SignForm, LoginForm
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def newqwest(request):
    user = request.user
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        raise Http404
    except TypeError:
        page = 1
    limit = 10
    qw = Question.objects.all()
    qw = Question.objects.new()
    paginator = Paginator(qw, limit)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'new_qw.html', {
        'us': user,
        'qw': page.object_list,
        'paginator': paginator, 'page': page,
    })

def popqwest(request):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        raise Http404
    limit = 10
    qw = Question.objects.all()
    qw = Question.objects.popular()
    paginator = Paginator(qw, limit)
    paginator.baseurl = '/popular/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'new_qw.html', {
        'qw': page.object_list,
        'paginator': paginator, 'page': page,
    })

def oneqwest(request, pk):
    qwest = get_object_or_404(Question, id=pk)
    ans = Answer.objects
    ans = ans.filter(question=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['question_id']
            answ = form.save()
            url = '/question/'+str(n)+'/'
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question_id': pk})
    return render(request, 'qwest.html', {
        'qwest' : qwest,
        'ans' : ans,
        'form': form
    })

def askfr(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            ask = form.save(commit=False)
            form._user = request.user.pk
            ask = form.save()
            url = ask.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm(initial={'author': int(request.user.pk)})
    return render(request, 'ask_add.html', {
        'form': form
    })

def signup(request):
    if request.method == "POST":
        form = SignForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            form = form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            url = '/'
            return HttpResponseRedirect(url)
    else:
        form = SignForm()
    return render(request, 'signup.html', {
        'form': form
    })

def loginus(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # Return a 'disabled account' error message
                print("The password is valid, but the account has been disabled!")
                return HttpResponseRedirect('/login/')
        else:
            print("The username and password were incorrect.")
            return HttpResponseRedirect('/login/')
    else:
         form = LoginForm()
    return render(request, 'login.html', {
        'form': form
    })

