from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Comments, FeedBack, ViewersProblem
from django.db import models

from django.forms.models import ModelForm

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = {
            "Email",
            "Subject",
            "Message"
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = {
            "Author",
            "Content",
            
        }
        widgets = {
            "Author": forms.TextInput(attrs={"class":"name"}),
            "Content": forms.Textarea(attrs={"class":"content"})
        }

class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = {
            "Author",
            "Content",
            
        }


class QuestionAskingForm(forms.ModelForm):
    class Meta:
        model = ViewersProblem
        fields = [
            'FullName',
            'Email',
            'Phone',
            'Problem',
            'Description'
        ]
        widgets= {
            'FullName': forms.TextInput(attrs={'class':'fullname', 'id':'fullname', 'placeholder':'fullname'}),
            'Email': forms.EmailInput(attrs={'class':'email','id':'email', 'placeholder':'Email'}),
            'Phone': forms.NumberInput(attrs={'class':'phone', 'id':'phone', 'placeholder':'Phone number'}),
            'Problem': forms.TextInput(attrs={'class':'problem', 'id':'problem', 'placeholder':'Your problem'}),
            'Description': forms.Textarea(attrs={'class':'description',"placeholder":"Description", 'name':'description', 'id':'description', 'cols':'100', 'rows':'5' })

            
        }

