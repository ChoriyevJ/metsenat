from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api import serializers
from api.models import Sponsor, Student, SponsorForStudent
#

class DashboardView(APIView):

    def get(self, request):
        students = Student.objects.all()
        sponsors = Sponsor.objects.all()



class SponsorCreateView(generics.CreateAPIView):
    queryset = None
    serializer_class = serializers.SponsorRUDSerializer


class SponsorsListView(generics.ListAPIView):
    queryset = Sponsor.objects.all()[:10]
    serializer_class = serializers.SponsorSerializer

    def get_queryset(self):
        fields = dict()
        for param in self.request.query_params:
            fields[param] = self.request.query_params.getlist(param)[0]

        return Sponsor.objects.filter(**fields)[:10]


class SponsorRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = serializers.SponsorRUDSerializer



class StudentCreateView(generics.CreateAPIView):
    queryset = None
    serializer_class = serializers.StudentSerializer


class StudentsListView(generics.ListAPIView):
    queryset = Student.objects.all()[:10]
    serializer_class = serializers.StudentSerializer

    def get_queryset(self):
        fields = dict()
        for param in self.request.query_params:
            fields[param] = self.request.query_params.getlist(param)[0]

        return Student.objects.filter(**fields)[:10]


class StudentRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentRUDSerializer


class CreateSponsorForStudent(generics.CreateAPIView):
    serializer_class = serializers.AddSponsorSerializer

    def post(self, request, pk):

        student = get_object_or_404(Student, pk=pk)
        data = request.data.copy()
        data['student'] = str(pk)
        if student:
            serializer = serializers.AddSponsorSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response(status=status.HTTP_404_NOT_FOUND)


class RUDSponsorForStudent(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AddSponsorSerializer
    queryset = SponsorForStudent











        



