from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:4]
    resp = ', '.join([q.question_text for q in latest_questions])
    return HttpResponse(resp)

def detail(request, question_id):
    return HttpResponse("This detail page %s" % question_id)

def results(request, question_id):
    return HttpResponse("This results page %s" % question_id)

def vote(request, question_id):
    return HttpResponse("This vote page %s" % question_id)