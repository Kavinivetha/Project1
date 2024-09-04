from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("index",views.index,name="home"),
    path("about",views.about,name="index"),
    path("bookappointment",views.bookappointment,name="bookappointment"),
    path("service",views.service,name="service"),
    path("contact",views.contact,name="contact"),
    path("feature",views.feature,name="feature"),
    path("team",views.team,name="team"),
    path("appointment",views.appointment,name="appointment"),
    path("testimonial",views.testimonial,name="testimonial"),
    path("error",views.error,name="404"),
    path("sendmessage",views.sendmessages,name="sendmessage"),
    path("confirmed",views.confirmed,name="confirmed"),
]