from rest_framework import serializers, pagination
from .models import Person, Reunion, Hobby

class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')


class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    activo = serializers.BooleanField(required=False)


#ejemplos pra agregar campos a model serializers sin dejar de utilizar el model
class PersonSerializers2(serializers.ModelSerializer):
    activo = serializers.BooleanField(default=False)
    class Meta:
        model = Person
        fields = ('__all__')


#serializer para reunion
class ReunionSerializer(serializers.ModelSerializer):

    perona = PersonSerializers()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'perona',

        )



class HobbySerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Hobby
        fields = ('__all__')


class PersonSerializers3(serializers.ModelSerializer):

    hobbies= HobbySerializers(many=True)

    class Meta:
        model = Person
        fields = (
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created',
            
        )




class ReunionSerializer2(serializers.ModelSerializer):

    fecha_hora = serializers.SerializerMethodField()
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'perona',
            'fecha_hora',

        )

    def get_fecha_hora(self, obj):
        return str(obj.fecha) + '-' + str(obj.hora)
        





class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'perona',              
        )
        extra_kwargs={
            'perona': {'view_name': 'persona_app:detalle', 'lookup_field': 'pk'}
        }


class PersonPagination(pagination.PageNumberPagination):
    page_size= 5
    max_page_size = 100



class CountReunionSerializer(serializers.Serializer):
    perona__job = serializers.CharField()
    cantidad = serializers.IntegerField()
   