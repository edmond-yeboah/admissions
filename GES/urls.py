from django.urls import path
from GES import views

urlpatterns = [
    path('',views.home,name="home"),
    path('schools',views.schools,name="schools"),
    path('courses',views.courses,name="courses"),
    path('search',views.search,name="search"),
    path('school-details',views.school_details,name="school_details"),
    path('course-details',views.course_details,name="course_details"),
]
