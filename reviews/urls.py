from django.urls import path

from . import views

urlpatterns = [
    path('', views.ReviewsView.as_view(), name='reviewslist'),
    path('<int:pk>/', views.FullReviewView.as_view(), name='reviewdetail'),
]