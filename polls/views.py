from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import *
# Create your views here.

def logout(request):
    request.session['userid'] = None
    request.session.clear()
    return HttpResponse('11')

def login(request):
    return render(request, 'polls/login.html')

def login_post(request):
    user_id = request.GET.get('user_id')
    user_pw = request.GET.get('user_pw')
    #print(user_id, user_pw)
    request.session['user_id'] = user_id  
    return HttpResponse(user_id+"님, 반갑습니다.")


def index(request):    
    latest_question_list = Question.objects.order_by('pub_date')[:5]    
    # output = ', '.join([q.question_text for q in latest_question_list])    
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return HttpResponse(output)
    return render(request,'polls/index.html',{'latest_question_list' : latest_question_list})

def detail(request, question_id):  # 질문 상세 페이지    
    try:
        question = Question.objects.get(id=question_id)
    except:
        pass
    else:
        return render(request,'polls/detail.html',{'question' : question})

def results(request, question_id):  # 투표 결과 페이지    
    response = "You're looking at the results of question %s."    
    return HttpResponse(response % question_id)

def vote(request, question_id):  # 투표 페이지    
    # 질문 조회
    # POST['choice'] 시 값이 없으면 동작이 죽어버림
    choice_id = request.POST.get('choice')
    question = get_object_or_404(Question, id=question_id)

    try:  # 보기 조회
        choice = question.choice_set.get(id=choice_id)
    
    except(KeyError, Choice.DoesNotExist):
        pass
        # return render(request, 'polls/exception.html', {})
    else:
        choice.votes += 1
        choice.save()

    # return HttpResponseRedirect('/polls/%s'%question_id)
    return HttpResponseRedirect(reverse('detail', args=(question.id,)))
    
def reset(request, question_id):

    question = Question.objects.get(pk=question_id)
    c_list = question.choice_set.all()
    
    for choice in c_list:
        choice.votes = 0
        choice.save()

    return HttpResponseRedirect(reverse('detail', args=(question.id,)))

def ajax1(request):
    return render(request, 'polls/ajax.html')

def ajax2(request):
    return render(request, 'polls/ajax2.html')
    
def ajax3(request):
    return render(request, 'polls/ajax3.html')