from django.urls import path
from . import views
urlpatterns = [
    path('', views.list_student, name="home"),
    path('update/<int:id>', views.update_student, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
]
