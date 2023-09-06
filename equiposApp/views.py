from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from equiposApp.models import Equipos
from equiposApp.serializers import EquiposSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def equipos_list(request):

    # GET - Obtener todos los equipos
    if request.method == 'GET':
        equipos = Equipos.objects.all()

        name = request.GET.get('name',None)
        if name is not None:
            equipos = equipos.filter(name_icontains=name)

        equipos_serializer = EquiposSerializer(equipos,many=True)
        return JsonResponse(equipos_serializer.data,safe=False)
    
    # POST - Crear equipo
    elif request.method == 'POST':
        equipos_data = JSONParser().parse(request)
        equipos_serializer = EquiposSerializer(data=equipos_data)

        if equipos_serializer.is_valid():
            equipos_serializer.save()
            return JsonResponse(equipos_serializer.data, status = status.HTTP_201_CREATED)
    
    return JsonResponse(equipos_serializer.data, status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def equipos_detail(request,pk):
    try:
        equipos = Equipos.objects.get(pk=pk)
    except Equipos.DoesNotExist:
        return JsonResponse({'Mensaje':'El equipo solicitado no existe'},status= status.HTTP_404_NOT_FOUND)

    # GET - Obtener un solo equipo
    if request.method == 'GET':
        equipos_serializer = EquiposSerializer(equipos)
        return JsonResponse(equipos_serializer.data)
    
    # PUT - Actualizar/Modificar un equipo
    elif request.method == 'PUT':
        equipos_data = JSONParser().parse(request)
        equipos_serializer = EquiposSerializer(equipos, data = equipos_data)

        if equipos_serializer.is_valid():
            equipos_serializer.save()
            return JsonResponse(equipos_serializer.data)
        return JsonResponse(equipos_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # DELETE - Borrar equipo
    elif request.method == 'DELETE':
        equipos.delete()
        return JsonResponse({'Mensaje':'El equipo ha sido borrado'}, status = status.HTTP_204_NO_CONTENT)