
from django.urls import path
from .views import InternshipListCreateView,InternshipDetailView,InternshipApplicationListCreateView

urlpatterns = [
    path('internships/', InternshipListCreateView.as_view(), name='internship-list-create'),
    path('internships/<int:pk>/', InternshipDetailView.as_view(), name='internship-detail'),
    path('applications/', InternshipApplicationListCreateView.as_view(), name='internship-application-list-create'),
    # path('api/upload/', ResumeUploadView.as_view(), name='file-upload'),

]
