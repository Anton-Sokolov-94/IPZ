from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from BrainStorm.models import Courses, Lecturers
import random

from BrainStorm.forms import SessionForm
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required()
def create(request):
    form = SessionForm()
    if request.POST['content'] != "" and request.GET['course'] != "":
        Lecturers(title = request.POST['title'], course_id = request.GET['course'], text = request.POST['content']).save()

    return render_to_response('edit.html', {
        'form': form, 'course': request.GET['course'],
    }, context_instance=RequestContext(request))


from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from BrainStorm.models import Courses, Lecturers, StudentsCourses, Comments, UserProfile
from django.contrib import sessions
import datetime


def index(request):
     return  render(request, "index.html")


def get_course(request): #FIX:
    template = loader.get_template("courses.html")
    return StreamingHttpResponse(template.render())

    '''
    lectures = []
    comments = []
    for each in Lecturers.objects.all():
        if each.course_id == int(request.GET['course']):
            lectures.append(each)

    go_corect = UserProfile.objects.get(pk=request.user.id).user_type

    if request.user.id != None:
        try: request.POST['comment']
        except BaseException: print "lol"
        else:
            Comments.objects.create(text = request.POST['comment'], user_name = request.user.username,
                                    course = Courses.objects.get(pk=request.GET['course'])).save()

    try:Comments.objects.filter(course=int(request.GET['course']))
    except BaseException:
        go_corect = (Courses.objects.get(pk=request.GET['course']).lector.id == request.user.id)
        course = Courses.objects.get(pk=int(request.GET['course']))
        context = Context({"course":course, "lectures": lectures, "type": go_corect})
        template = loader.get_template("course.html")
        return StreamingHttpResponse(template.render(context))

    if Comments.objects.filter(course_id=int(request.GET['course'])).__len__() == 1:
        comments.append(Comments.objects.get(course_id=int(request.GET['course'])))
    else:
        comments = Comments.objects.filter(course_id=int(request.GET['course']))

    course = Courses.objects.get(pk=request.GET['course'])
    context = Context({"course":course, "lectures": lectures, "comments": comments, "type": go_corect})
    template = loader.get_template("course.html")
    return StreamingHttpResponse(template.render(context))

    '''


def find_courses(request):###########################    FIND COURSE!!!!    ##########################
    context = []
    courses = []
    if request.method == 'POST':
        if request.POST['course'] == '':
            for each in Courses.objects.all():
                    courses.append(each)

            con = Context({'courses':courses})
            template = loader.get_template("courses.html")
            return StreamingHttpResponse(template.render(con))
        else:
            for each in Courses.objects.all():
                if each.title.find(request.POST['course']) != -1:
                    courses.append(each)
                    print(each.title)

            if courses.__len__() == 0:
                for each in Courses.objects.all():
                    context.append(each)

                error = 'Wrong course name!'
                con = Context({'error':error, 'courses':context})
                template = loader.get_template("courses.html")
                return StreamingHttpResponse(template.render(con))
            else:
                con = Context({'courses':courses})
                template = loader.get_template("courses.html")
                return StreamingHttpResponse(template.render(con))

    for each in Courses.objects.all():
        courses.append(each)
    con = Context({'courses':courses})
    template = loader.get_template("courses.html")
    return StreamingHttpResponse(template.render(con))



def main( request ):
    template = loader.get_template("main.html.html")
    c = Context()
    return StreamingHttpResponse(template.render(c))

def subscribe_on_course(request):
    message = 'You are already subscribed to course!'

    if request.user.id == None:
        return HttpResponseRedirect('/accounts/login/')

    s_id = request.user.id
    c_id = int(request.GET['course'])
    try:
        StudentsCourses.objects.get(student_id = s_id, course_id = c_id)
    except BaseException:
        membership = StudentsCourses.objects.create(student_id=s_id, course_id = c_id, subscribe_date=datetime.datetime.now())
        membership.save()
        message = "Congratulation! You have successfully subscribed!"

    template = loader.get_template("subscribe.html")
    c = Context({'message':message})
    return StreamingHttpResponse(template.render(c))

def unsubscribe(request):  ######################## Unsubscribe! ######################################
    c_id = request.GET['course']
    s_id = request.user.id

    StudentsCourses.objects.get(course_id=c_id, student_id=s_id).delete()
    return HttpResponseRedirect('/')

def get_lecture(request):

    error = ''

    if request.user.id == None:
        return HttpResponseRedirect('/accounts/login/')

    s_id = request.user.id
    c_id = int(Lecturers.objects.get(pk=int(request.POST['lecture'])).course.id)

    if UserProfile.objects.get(pk=request.user.id).user_type:
        try:
            StudentsCourses.objects.get(student_id = s_id, course_id = c_id)
        except BaseException:
            error = 'Please subscribe on the course!'
            template = loader.get_template("lecture.html")
            con = Context({'error':error})
            return StreamingHttpResponse(template.render(con))

    lecture = Lecturers.objects.get(pk=int(request.POST['lecture']))
    temp = "{% extends 'lecture.html' %} {% block lecture %}"
    temp += lecture.text
    temp += "{% endblock %}"
   # template = loader.Template("")
    template = loader.Template(temp)
    con = Context({'lecture':lecture})
    return StreamingHttpResponse(template.render(con))