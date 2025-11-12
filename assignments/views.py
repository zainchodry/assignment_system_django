from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Assignment, Submission
from .forms import AssignmentForm, SubmissionForm
from courses.models import Course

@login_required
def assignment_list(request):
    if request.user.role == 'teacher':
        assignments = Assignment.objects.filter(course__created_by=request.user)
    else:
        assignments = Assignment.objects.filter(course__enrollments__student=request.user).distinct()
    return render(request, 'assignment_list.html', {'assignments': assignments})


@login_required
def create_assignment(request):
    if request.user.role != 'teacher':
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            if assignment.course.created_by != request.user:
                return HttpResponseForbidden("You are not allowed to add assignments to this course.")
            assignment.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm()
        form.fields['course'].queryset = Course.objects.filter(created_by=request.user)
    return render(request, 'create_assignment.html', {'form': form})


@login_required
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)

    enrolled = assignment.course.enrollments.filter(student=request.user).exists()
    if not enrolled or request.user.role != 'student':
        return HttpResponseForbidden("You are not enrolled in this course.")

    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission, created = Submission.objects.get_or_create(
                assignment=assignment, student=request.user,
                defaults={'file': form.cleaned_data['file']}
            )
            if not created:
                submission.file = form.cleaned_data['file']
                submission.save()
            return redirect('assignment_list')
    else:
        form = SubmissionForm()
    return render(request, 'submit_assignment.html', {'form': form, 'assignment': assignment})


@login_required
def submission_list(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if assignment.course.created_by != request.user:
        return HttpResponseForbidden()
    submissions = assignment.submissions.all()
    return render(request, 'submission_list.html', {'assignment': assignment, 'submissions': submissions})


@login_required
def grade_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    if submission.assignment.course.created_by != request.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        grade = request.POST.get('grade')
        feedback = request.POST.get('feedback')
        submission.grade = grade
        submission.feedback = feedback
        submission.save()
        return redirect('submission_list', assignment_id=submission.assignment.id)
    return render(request, 'view_submission.html', {'submission': submission})
