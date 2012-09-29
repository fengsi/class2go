from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.template import Context, loader
from c2g.models import *
from courses.common_page_data import get_common_page_data
from courses.actions import auth_is_course_admin_view_wrapper

@auth_is_course_admin_view_wrapper
def reorder(request, course_prefix, course_suffix):
    try:
        common_page_data = get_common_page_data(request, course_prefix, course_suffix)
    except:
        raise Http404
    
    if not common_page_data['is_course_admin']:
        return redirect('courses.views.main',  course_prefix, course_suffix)
        
    sections = ContentSection.objects.getByCourse(course=common_page_data['course'])
    
    return render(request, 'content_sections/draft/reorder.html', {
        'common_page_data': common_page_data,
        'sections': sections
    })

@auth_is_course_admin_view_wrapper
def rename(request, course_prefix, course_suffix, section_id):
    try:
        common_page_data = get_common_page_data(request, course_prefix, course_suffix)
    except:
        raise Http404
    
    if not common_page_data['is_course_admin']:
        return redirect('courses.views.main',  course_prefix, course_suffix)
        
    section = ContentSection.objects.get(id=section_id)
    return render(request, 'content_sections/draft/rename.html', {
        'common_page_data': common_page_data,
        'section': section
    })
