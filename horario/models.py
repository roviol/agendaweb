from django.db import models

# Create your models here.
class Colegio(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return u"%s" % (self.nombre)

