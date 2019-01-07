# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from models import Question, Answer
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET

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

@require_GET
def oneqwest(request, pk):
    qwest = get_object_or_404(Question, id=pk)
    ans = Answer.objects
    ans = ans.filter(question=pk)
    return render(request, 'qwest.html', {
        'qwest' : qwest,
        'ans' : ans
    })

