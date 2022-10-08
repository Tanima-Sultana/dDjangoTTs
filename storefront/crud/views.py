from functools import partial
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from account import serializers
from .models import Student
from account.serializers import StudentSerializer
from django .http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# for generic APIView and MOdelMixin
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin
from rest_framework.generics import GenericAPIView


#  Here pk is not required for create and list mixins
class GenericMixinStudentListAndCreate(GenericAPIView, ListModelMixin,CreateModelMixin):
    """ Generic Mixin based api view classes  """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs ):
        return self.list(request,*args, **kwargs)

    def post(self, request, *args, **kwargs ):
        return self.create(request,*args, **kwargs)

# class GenericMixinStudentCreate(GenericAPIView, CreateModelMixin):
#     """ Generic Mixin based api view classes  """
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def post(self, request, *args, **kwargs ):
#         return self.create(request,*args, **kwargs)

# For retrieve, update and delete PK is needed
class GenericMixinStudentRetrieveUpdateDestroy(GenericAPIView, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin):
    """ Generic Mixin based api view classes  """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs ):
        return self.retrieve(request,*args, **kwargs)
    def put(self, request, *args, **kwargs ):
        return self.update(request,*args, **kwargs)

    def delete(self, request, *args, **kwargs ):
        return self.destroy(request,*args, **kwargs)

# class GenericMixinStudentUpdate(GenericAPIView, UpdateModelMixin):
#     """ Generic Mixin based api view classes  """
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def put(self, request, *args, **kwargs ):
#         return self.update(request,*args, **kwargs)

# class GenericMixinStudentDestroy(GenericAPIView, DestroyModelMixin):
#     """ Generic Mixin based api view classes  """
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def delete(self, request, *args, **kwargs ):
#         return self.destroy(request,*args, **kwargs)
    """ class based api views all the crud operation is described here """
class StudentAPI(APIView):
    def get(self, request, pk=None,format = None):
        id = pk
        print('id',id)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)

    def post(self, request, pk = None, format = None):
        data = request.data
        serializer = StudentSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response( {'mgs':'Data Created'} , status=status.HTTP_201_CREATED)

        print(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk , format = None):
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu,data = request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mgs':'Complete Data Updated','data':serializer.data})

        print(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk ,format = None):
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu,data = request.data, partial = True)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mgs':'Partial Data Updated','data':serializer.data})

        print(request.data)
        return Response(serializer.errors)
        
    def delete(self, request, pk, format = None):
        id = pk
        stu = Student.objects.get(pk = id)
        stu.delete()
        return Response({'mgs':'Data Deleted!'})



""" function based api views all the crud operation is described here"""

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def function_based_student_api(request,pk= None):
    if request.method == 'GET':
        id = pk
        print('id',id)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        serializer = StudentSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response( {'mgs':'Data Created'} , status=status.HTTP_201_CREATED)

        print(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu,data = request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mgs':'Complete Data Updated','data':serializer.data})

        print(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu,data = request.data, partial = True)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mgs':'Partial Data Updated','data':serializer.data})

        print(request.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk = id)
        stu.delete()
        return Response({'mgs':'Data Deleted!'})



""" normal crud operation, tested on running myapp python file"""
@csrf_exempt
def get_student(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream=stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')
        stu = Student.objects.all()
        serialize = StudentSerializer(stu, many = True)
        json_data = JSONRenderer().render(serialize.data)
        return HttpResponse(json_data, content_type = 'application/json')
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream=stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'mgs':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream=stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu,data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'mgs':'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream=stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {'mgs':'Data deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type = 'application/json')







