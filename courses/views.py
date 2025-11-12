from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment
from .forms import CourseForm

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enrolled = False
    if request.user.role == 'student':
        enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()
    return render(request, 'course_detail.html', {'course': course, 'enrolled': enrolled})

@login_required
def create_course(request):
    if request.user.role != 'teacher':
        return redirect('course_list')

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user
            course.save()
            return redirect('my_courses')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})

@login_required
def my_courses(request):
    if request.user.role == 'teacher':
        courses = Course.objects.filter(created_by=request.user)
    else:
        enrolled_ids = Enrollment.objects.filter(student=request.user).values_list('course_id', flat=True)
        courses = Course.objects.filter(id__in=enrolled_ids)
    return render(request, 'my_courses.html', {'courses': courses})

@login_required
def enroll_course(request, course_id):
    if request.user.role != 'student':
        return redirect('course_list')

    course = get_object_or_404(Course, id=course_id)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('my_courses')
