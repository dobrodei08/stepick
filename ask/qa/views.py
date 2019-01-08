# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from models import Question, Answer
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from forms import AskForm, AnswerForm
def test(request, *args, **kwargs):
    return HttpResponse('OK')


def newqwest(request):
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

def answ(request, pk):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answ = form.save()
            url = reverse('question', kwargs={'pk': pk})
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    return form



def oneqwest(request, pk):
    qwest = get_object_or_404(Question, id=pk)
    ans = Answer.objects
    ans = ans.filter(question=pk)
    form = answ(request, pk)
    return render(request, 'qwest.html', {
        'qwest' : qwest,
        'ans' : ans,
        'form': form
    })

def askfr(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            ask = form.save()
            url = ask.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask_add.html', {
        'form': form
    })
