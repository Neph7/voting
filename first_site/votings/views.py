from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


from django.http import HttpResponse
from .models import Question, Choice


def index(request):
    question_list = Question.objects.all()
    context = {'question_list':question_list}
    return render(request, 'votings/index.html',context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'votings/detail.html', {'question':question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return  HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)

    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):

        return render(request, 'votings/detail.html', {'question':question, 'error_message':"You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('votings:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)

    return render(request, 'votings/results.html', {'question':question})