from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse
from .models import Blogpost
from .forms import BlogpostForm,UserSignupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.tasks import send_welcome_mail

# Create your views here.
class BlogpostView(TemplateView):
    template_name="blog/index.html"
    def get(self,request):
        posts=Blogpost.objects.all()
        response=[{'id':post.id,
                   'title':post.title,
                   'author':post.author
                    } for post in posts]
        return self.render_to_response({'posts':response})
    
class BlogpostDetailView(TemplateView):
    template_name="blog/detail.html"
    def get(self,request,id):
        try:
            post=Blogpost.objects.get(id=id)
        except Blogpost.DoesNotExist:
            raise Http404("Blogpost not found")
        else:
            context={
                'id':post.id,
                'title':post.title,
                'author':post.author,   
                'body':post.body
            }
            return self.render_to_response(context)

class BlogpostCreateView(LoginRequiredMixin,TemplateView):
    template_name="blog/create.html"
    def get(self,request):
        form=BlogpostForm()
        return self.render_to_response({'form':form})
    
    def post(self,request):
        form=BlogpostForm(request.POST)
        if form.is_valid():
            blogpost=form.save(commit=False)
            blogpost.user=request.user
            blogpost.save()
            return HttpResponseRedirect(reverse('blog-detail',kwargs={'id':form.instance.id}))
        else:
            return self.render_to_response({'errors':form.errors})
        
class BlogpostUpdateView(LoginRequiredMixin,TemplateView):
    template_name="blog/update.html"
    def get(self,request,id):
        blogpost=get_object_or_404(Blogpost,id=id)
        if blogpost.user != request.user:
            raise Http404("You are not allowed to edit this post")
        form=BlogpostForm(instance=blogpost)
        return self.render_to_response({'form':form,'id':id})
    
    def post(self,request,id):
        blogpost=get_object_or_404(Blogpost,id=id)
        if blogpost.user != request.user:
            raise Http404("You are not allowed to edit this post")
        form=BlogpostForm(request.POST,instance=blogpost)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog-detail',kwargs={'id':form.instance.id}))
        else:
            return self.render_to_response({'errors':form.errors,'id':id})
        
class SignupView(TemplateView):
    template_name="blog/signup.html"
    def get(self,request):
        form=UserSignupForm()
        return self.render_to_response({'form':form})
    
    def post(self,request):
        form=UserSignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            send_welcome_mail.delay(user.email)
            return HttpResponseRedirect(reverse('blog'))
        else:
            return self.render_to_response({'form':form})