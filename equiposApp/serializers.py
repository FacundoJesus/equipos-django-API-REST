from rest_framework import serializers
from equiposApp.models import Equipos

class EquiposSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipos
        fields = ('id', 'nombre', 'fundacion', 'apodo', 'ciudad', 'nombre_estadio')
