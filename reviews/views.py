from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Review

# Create your views here.


def index(request):
    return HttpResponse("Hello, darkness. You're at the reviews index.")


class ReviewsView(ListView):
    model = Review
    context_object_name = 'salient_reviews_list'
    ordering = ['author']


class FullReviewView(DetailView):
    model = Review
