from django.urls import path
from api import views

urlpatterns = [
    path('sponsor/create/', views.SponsorCreateView.as_view(), name='sponsor_create'),
    path('sponsors/', views.SponsorsListView.as_view(), name='sponsors_list'),
    path('sponsor/<int:pk>/', views.SponsorRUDView.as_view(), name='sponsor_rud'),



    path('student/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/', views.StudentsListView.as_view(), name='students_list'),
    path('student/<int:pk>/', views.StudentRUDView.as_view(), name='student_rud'),

    path('student/<int:pk>/add-sponsor/', views.CreateSponsorForStudent.as_view(),
         name='sponsor_create_for_student'),
    path('student/<int:pk>/sponsor-rud/', views.RUDSponsorForStudent.as_view(),
         name='sponsor_rud_for_student')

]


