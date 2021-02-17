from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from ToDo_app.models import List
from ToDo_app.forms import NewListForm
from ToDo_app.searilizer import ListSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
    list=List.objects.all()
    form = NewListForm()
    if request.method == "POST":
        form = NewListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context={'list':list,'form':form}

    return render(request,'ToDo_app/list.html',context)


def updatetask(request, pk):
    task = List.objects.get(id=pk)

    form = NewListForm(instance=task)
    if request.method == "POST":
        form = NewListForm(request.POST , instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form':form}

    return render(request,'ToDo_app/update_item.html',context)

def deletetask(request, pk):
    item = List.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("/")

    context = {'item':item}
    return render(request,'ToDo_app/delete.html',context)


class GenericList(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    serializer_class = ListSerializer
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = List.objects.all()
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class GenericDetail(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
        serializer_class = ListSerializer
        #authentication_classes = [SessionAuthentication, BasicAuthentication]
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        queryset = List.objects.all()
        lookup_field = 'id'

        def get(self, request, id = None):
            if id:
                return self.retrieve(request)
            else:
                return self.list(request)

        def put(self, request, id = None):
            return self.update(request, id)

        def delete(self, request, id=None):
            return self.destroy(request, id)






class ListList(APIView):
    def get(self, request):
        myList=List.objects.all()
        serial = ListSerializer(myList, many = True)
        return Response(serial.data)

    def post(self, request):
        serial = ListSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status= status.HTTP_201_CREATED)

        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class ListDetail(APIView):
    def get_object(self,pk):
        try:
            return List.objects.get(pk=pk)
        except List.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        li = self.get_object(pk)
        serial = ListSerializer(li)
        return Response(serial.data)

    def put(self,request, pk):
        li = self.get_object(pk)
        serial = ListSerializer(li, request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        li = self.get_object(pk)
        li.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)








@api_view(['GET', 'POST'])
def appList_list(request):
    if request.method =="GET":
        myList=List.objects.all()
        serial = ListSerializer(myList, many = True)
        return Response(serial.data)

    elif request.method ==  "POST":
        serial = ListSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status= status.HTTP_201_CREATED)

        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def list_detail(request,pk):
    try:
        li = List.objects.get(pk=pk)

    except List.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = ListSerializer(li)
        return Response(serial.data)

    elif request.method == 'PUT':
        serial = ListSerializer(li, request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        li.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
