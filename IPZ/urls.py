from django.conf.urls import patterns, include, url
from BrainStorm.views import *
from profiles.signals import *
from django.contrib import admin
from registration.backends.default.views import RegistrationView
from django.conf.urls.static import static
from django.conf import settings
from profiles.form import ProfileForm

admin.autodiscover()


urlpatterns = patterns('',

    url('^$', main),
    url('^index/',index),
    url('courses/$', find_courses),
    url('^profiles/edit', 'profiles.views.edit_profile', {'form_class': ProfileForm,}),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^editor/',create),
    url('courses/$', find_courses),
    url('courses/course$', get_course),
    url('courses/course/lecture$', get_lecture),
    url('courses/subscribe$', subscribe_on_course),
    url('courses/unsubscribe$', unsubscribe),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class = RegistrationFormProfile) ,name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/docs', include('django.contrib.admindocs.urls')),
)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

