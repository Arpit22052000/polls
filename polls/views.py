from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Question, Choice
from django.urls import reverse

from django.views import generic
from .forms import AddQuestionForm

# Create your views here.


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-publication_date")


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/vote",
            {"question": question, "error_message": "Ypu didn't selected a choice."},
        )

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def add(request):
    if request.method == "POST":
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            question_value = form.cleaned_data["question_text"]
            form.save()
            return redirect("success_url")

    else:
        form = AddQuestionForm()

    return render(request, "polls/add.html", {"form": form})
