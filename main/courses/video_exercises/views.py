from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

from c2g.models import Video
from courses.actions import auth_view_wrapper

@auth_view_wrapper
def view(request, course_prefix, course_suffix, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'video_exercises/view.html', {
        'course_prefix': course_prefix,
        'course_suffix': course_suffix,
        'video': video
    })
