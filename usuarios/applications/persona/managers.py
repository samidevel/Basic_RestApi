from django.db import models
from django.db.models import Count

class ReunionManager(models.Manager):
    def cantidad_reuniones_job(self):
        resultado = self.values('perona__job').annotate(
            cantidad=Count('id')   
        )
        print("resultado")
        print(resultado)
        return resultado