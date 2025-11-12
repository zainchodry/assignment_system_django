from django.urls import path
from . import views

urlpatterns = [
    path('', views.assignment_list, name='assignment_list'),
    path('create/', views.create_assignment, name='create_assignment'),
    path('<int:assignment_id>/submit/', views.submit_assignment, name='submit_assignment'),
    path('<int:assignment_id>/submissions/', views.submission_list, name='submission_list'),
    path('submission/<int:submission_id>/grade/', views.grade_submission, name='grade_submission'),
]
