from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from student.serializer import StudentSerializer,LoginSerializer,HolidaySerializer
from django.http import JsonResponse
from django.views.generic import View
from django.http import Http404,HttpResponseRedirect,JsonResponse
from django.http import JsonResponse
from student.models import Student,Holiday
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins,generics,status
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.decorators import detail_route
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'roll_no'
    # authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class HolidayViewSet(generics.GenericAPIView,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     ):
    serializer_class = HolidaySerializer
    queryset = Holiday.objects.all()
    lookup_field = 'roll_no'
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        return self.update(request)

    def delete(self,request,id=None):
        return self.destroy(request,id)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request,user)
        token,created = Token.objects.get_or_create(user=user)
        return Response({"token":token.key},status=200)

@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self,request):
        logout(request)
        return Response(status=204)

class CheckAPIView(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self,request):
        holidays = Holiday.objects.all()
        serializer = HolidaySerializer(holidays,many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = HolidaySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

    def get_object(self, id):
        try:
            return Holiday.objects.get(id=id)
        except Holiday.DoesNotExist as e:
            return Response({"error": "Given question not found"}, status=404)

    def put(self,request,id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = HolidaySerializer(instance,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)
