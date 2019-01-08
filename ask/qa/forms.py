from django import forms
from models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    def clean_text(self):
        text = self.cleaned_data['text']
        return text
    def clean_title(self):
        title = self.cleaned_data['title']
        return title
    def save(self):
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
    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
