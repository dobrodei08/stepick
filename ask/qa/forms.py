from django import forms
from models import Question, Answer
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    def clean_username(self):
        username = self.cleaned_data['username']
        return username
    def clean_password(self):
        password = self.cleaned_data['password']
        return password

class SignForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    def clean_username(self):
        username = self.cleaned_data['username']
        return username
    def clean_email(self):
        email = self.cleaned_data['email']
        return email
    def clean_password(self):
        password = self.cleaned_data['password']
        return password
    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return user

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    def clean_text(self):
        text = self.cleaned_data['text']
        return text
    def clean_title(self):
        title = self.cleaned_data['title']
        return title
    def save(self, commit=True):
        question  = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question_id = forms.IntegerField(widget=forms.HiddenInput())
    def clean_text(self):
        text = self.cleaned_data['text']
        return text
    def clean_question(self):
        question_id = self.cleaned_data['question_id']
        return question_id
    def save(self, commit=True):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
