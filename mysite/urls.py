from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from lms.urls import student_router



urlpatterns = [
    path('admin/', admin.site.urls),
    path('lms/', include(student_router.urls)),
]
