# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=200)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='u', blank=True, null=True)
    def get_url(self):
        return reverse('question',
        kwargs={'pk': self.id})

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(default=timezone.now)
    question = models.ForeignKey(Question,on_delete=models.CASCADE,blank=True, null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)

