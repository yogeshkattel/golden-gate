from django.core.checks import messages
from django.db import models
from django.http import response
from django.shortcuts import redirect, render
from django.utils.html import format_html
from django.views.generic import TemplateView, ListView, View
from .forms import * 
from django.views.generic.detail import DetailView
from django.core.mail import send_mail
# Create your views here.
from .models import *
from django.conf import settings

# this is inded page faq is a model and listview is used to list data in faq
class Home(TemplateView):
    template_name = 'index.html'


#this is a blogist page this page lists all the available blogs
class BlogView(ListView):
    model = Blog
    template_name = "diseases.html"
    context_object_name = "blog"
    
#this is a singleblog page which shows the data of a specific blog that user visits
class BlogDetailView(View):

    def get(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        comments = Comments.objects.filter(Blog=blog).order_by('DateTime').all()
        form = CommentForm
       
        context = {
            "blog":blog,
            "comments":comments,
            "form":form,
            
        }
        return render(request, "disease_detail.html", context)
        
    def post(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        slugs = blog.slug
        form = CommentForm(request.POST)
        
        if form.is_valid:
            comment = form.save(commit=False)
            comment.Blog = blog
            comment.save()
        
        context = {
            "blog":blog,
            "form":form,
           
        }
        return redirect(F"/blog/{slugs}/detail")


class CommentReplyView(View):
    def post(self, request, pk, slug ,*args, **kwargs):
        form = CommentForm(request.POST)
        blog = Blog.objects.get(slug=slug)
        slugs = blog.slug
        parent_comment = Comments.objects.get(pk=pk)

        if form.is_valid():
            reply = form.save(commit=False)
            reply.Blog = blog
            reply.Parent = parent_comment
            reply.save()

        return redirect(F"/blog/{slugs}/detail")
           


#This is contact us page 
class contactus(View):
    #get method to render form inn html
    def get(self, request, *args, **kwargs):
        form = FeedbackForm

        return render(request, "contactus.html", {'form':form})
    # post method for fetching entered data from frontend
    
    
    def post(self, request, *args, **kwargs):
        #fetching form data
        form= FeedbackForm (request.POST)
        email = form.data.get("Email")
        subject = form.data.get("Subject")
        message = form.data.get("Message")
        if form.is_valid:
            form.save()
            send_mail(
                subject="Thankyou message",
                message="Thankyou for sending us your feedback Means a lot for us." ,
                from_email = settings.EMAIL_HOST_USER,
                recipient_list= [email,]
            )
            send_mail(
                subject,
                message + email,
                email,
                [settings.EMAIL_HOST_USER,]
            )
                
            
            
        return render(request, "contactus.html", {'form':form})


class ViewersProblemsView(View):
    def get(self, request):
        form = QuestionAskingForm
        return  render(request, "queries.html", {"form":form})
    
    def post(self, request):
        form = QuestionAskingForm(request.POST)
        Name = form.data.get("FullName")
        email = form.data.get("Email")
        Phone = form.data.get("Phone")
        Problem = form.data.get("Problem")
        Description = form.data.get("Description")
        if form.is_valid:
            form.save()
            send_mail(
                subject="Thankyou for sending us your queries",
                message="Thankyou for sending us your queries owr docutor will contact you personnally shortly." ,
                from_email = settings.EMAIL_HOST_USER,
                recipient_list= [email,]
            )
            send_mail(
                Problem,
                Description + email,
                email,
                [settings.EMAIL_HOST_USER,]




            )

        return render(request, "queries.html", {"form":form})
            
    
