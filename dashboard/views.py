from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import Course, Enrollment
from assignments.models import Assignment, Submission
from django.utils import timezone

@login_required
def dashboard_view(request):
    if request.user.role == 'teacher':
        courses = Course.objects.filter(created_by=request.user)
        assignments = Assignment.objects.filter(course__in=courses)
        submissions = Submission.objects.filter(assignment__in=assignments)
        context = {
            'courses_count': courses.count(),
            'assignments_count': assignments.count(),
            'submissions_count': submissions.count(),
            'recent_submissions': submissions.order_by('-submitted_at')[:5]
        }
        return render(request, 'dashboard_teacher.html', context)

    else:
        enrollments = Enrollment.objects.filter(student=request.user)
        courses = [en.course for en in enrollments]
        assignments = Assignment.objects.filter(course__in=courses, due_date__gte=timezone.now()).order_by('due_date')
        submissions = Submission.objects.filter(student=request.user)
        context = {
            'enrolled_courses': courses,
            'upcoming_assignments': assignments,
            'my_submissions': submissions,
        }
        return render(request, 'dashboard_student.html', context)
