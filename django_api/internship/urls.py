
from django.urls import path
from .views import InternshipListCreateView,InternshipDetailView

urlpatterns = [
    path('internships/', InternshipListCreateView.as_view(), name='internship-list-create'),
    path('internships/<int:pk>/', InternshipDetailView.as_view(), name='internship-detail'),

]
