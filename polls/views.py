from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Este é meu primeiro site utilizando django")



def detail(request,question_id):
    return HttpResponse("Voçê esta olhando para pergunta %s" %question_id)

def results(request, question_id):
    response = "Voçê esta olhando para pergunta %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Você esta votando na pergunta %s" %question_id)

from .models import Question

def index(request):
    latest_question_list = Question.objects.order.by("-pub_date")[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

