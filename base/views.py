from http.client import HTTPResponse
from django.shortcuts import render, redirect
from . models import Questions, choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse



# Create your views here.
def home(request):
    return render(request, 'index.html')
    
def index(request):
    latest_questions = Questions.objects.order_by('-pub_date')[:5]
    context = {'latest_questions':latest_questions}
    return render(request,'base/index.html',context)



def detail(request,id):
    try:
        question = Questions.objects.get(pk=id)
    except Questions.DoesNotExist:
         HTTPResponse("Question does not exist")
        
    return render(request,'base/detail.html', {'question':question})   
     
def results(request,id):
    question = Questions.objects.get(pk=id)
    return render(request, 'base/results.html',{'question':question})


def vote(request, id):
    question = Questions.objects.get(pk=id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'base/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
  
        return redirect('base:index')