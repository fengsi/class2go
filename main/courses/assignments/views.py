from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

def list(request, course_prefix, course_suffix):
    return render(request, 'assignments/list.html', {
        'course_prefix': course_prefix,
        'course_suffix': course_suffix
    })

def admin(request, course_prefix, course_suffix):
    return render(request, 'assignments/admin.html', {
        'course_prefix': course_prefix,
        'course_suffix': course_suffix
    })
    
def view(request, course_prefix, course_suffix, assignment_id):
    return render(request, 'assignments/view.html', {
        'course_prefix': course_prefix,
        'course_suffix': course_suffix,
        'assignment_id': assignment_id
    })
    
def edit(request, course_prefix, course_suffix, assignment_id):
    return render(request, 'assignments/edit.html', {
        'course_prefix': course_prefix,
        'course_suffix': course_suffix,
        'assignment_id': assignment_id
    })
    
def grade(request, course_prefix, course_suffix, assignment_id):
    return render(request, 'assignments/grade.html', {
        'course_prefix': course_prefix,
        'course_suffix': course_suffix,
        'assignment_id': assignment_id
    })
