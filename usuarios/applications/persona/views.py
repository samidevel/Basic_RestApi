from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    
    
    


)
from django.views.generic import ListView, TemplateView




from . models import Person, Hobby, Reunion
from .serializers import (
    PersonSerializers,
    PersonaSerializer,
    PersonSerializers2,
    ReunionSerializer,
    PersonSerializers3,
    ReunionSerializerLink,
    PersonPagination,
    CountReunionSerializer

) 



class ListaPersonas(ListView):
    template_name = "persona/personas.html"
    context_object_name= "personas"

    def get_queryset(self):
        return Person.objects.all()




class PersonListApiview(ListAPIView):
    serializer_class = PersonSerializers

    def get_queryset(self):
        return Person.objects.all()



class PersonListView(TemplateView):
    template_name = 'persona/lista.html'



class PersonSearchApiView(ListAPIView):
    serializers_class = PersonSerializers

    def get_queryset(self):
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains = kword
        )


class PersonCreateView(CreateAPIView):
    serializer_class = PersonSerializers

class PersonDetailView(RetrieveAPIView):

    serializer_class = PersonSerializers
    queryset = Person.objects.all()

class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonSerializers

    queryset = Person.objects.all()


class PersonUpdateView(UpdateAPIView):
    serializer_class = PersonSerializers
    queryset = Person.objects.all()
    


class PersonRetreaveUpdateView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializers
    queryset = Person.objects.all()



class PersonApiLista(ListAPIView):
    #serializer_class = PersonaSerializer
    serializer_class = PersonSerializers3

    def get_queryset(self):
        return Person.objects.all()
    

    
class ReunionApiLista(ListAPIView):
    serializer_class = ReunionSerializer

    def get_queryset(self):
        return Reunion.objects.all()
    

class ReunionApiListaLink(ListAPIView):
    serializer_class = ReunionSerializerLink

    def get_queryset(self):
        return Reunion.objects.all()
    




class PersonPaginationLists(ListAPIView):
    """""
    paginacion
    """""
    serializer_class = PersonaSerializer
    pagination_class = PersonPagination
    def get_queryset(self):
        return Person.objects.all()
    


class ReunionByPersonJob(ListAPIView):
    serializer_class =  CountReunionSerializer

    def  get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()