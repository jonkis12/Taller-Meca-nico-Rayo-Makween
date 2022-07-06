from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Trabajo
from .serializers import TrabajoSerializer
from django.shortcuts import get_object_or_404




@csrf_exempt
@api_view(['GET', 'POST'])

def lista_trabajos(request):
    if request.method == 'GET':
        lista = Trabajo.objects.all()
        serializer = TrabajoSerializer(lista, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TrabajoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])

def detalle_trabajo(request,id):
    try:
        trabajo = Trabajo.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TrabajoSerializer(trabajo)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TrabajoSerializer(trabajo, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        trabajo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
    
class TrabajoViewSet(viewsets.ModelViewSet):
    queryset = Trabajo.objects.all()
    serializer_class = TrabajoSerializer
    
    def list(self, request):
        queryset = Trabajo.objects.all()
        serializer = TrabajoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        u = request.user
        queryset = Trabajo.objects.filter(user = u, pk = pk)
        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = TrabajoSerializer(queryset)
            return Response(serializer.data,status=status.HTTP_200_OK)


    
