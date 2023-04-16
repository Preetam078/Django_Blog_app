from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.student_api),
    path('student/<int:id>/', views.student_apiParams)
]
