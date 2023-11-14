
from django.urls import path
from .views import InternshipListCreateView

urlpatterns = [
    path('internships/', InternshipListCreateView.as_view(), name='internship-list-create'),
]
