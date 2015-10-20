from django.db import models
import myFields

DAYS_OF_WEEK = (
    ('0', 'Domingo'),
    ('1', 'Lunes'),
    ('2', 'Martes'),
    ('3', 'Miercoles'),
    ('4', 'Jueves'),
    ('5', 'Viernes'),
    ('6', 'Sabado'),
)

class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return u"%s" % (self.nombre)
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Paises'

class Ciudad(models.Model):
    pais = models.ForeignKey(Pais)
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return u"%s" % (self.nombre)
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Ciudades'

class Colegio(models.Model):
    ciudad = models.ForeignKey(Ciudad)
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return u"%s" % (self.nombre)
    class Meta:
        ordering = ['nombre']

class Curso(models.Model):
    colegio = models.ForeignKey(Colegio)
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return u"%s" % (self.nombre)
    class Meta:
        ordering = ['nombre']

class Seccion(models.Model):
    curso = models.ForeignKey(Curso)
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return u"%s" % (self.nombre)
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Secciones'

class Materia(models.Model):
    curso = models.ForeignKey(Curso)
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return u"%s" % (self.nombre)
    class Meta:
        ordering = ['nombre']

class MateriaCurso(models.Model):
    curso = models.ForeignKey(Curso)
    materia = models.ForeignKey(Materia)
    def __unicode__(self):
        return u"%s %s" % (self.curso.nombre, self.materia.nombre)

class Horario(models.Model):
    seccion = models.ForeignKey(Seccion)
    desde = models.DateField()
    hasta = models.DateField()
    def __unicode__(self):
        return u"%s %s%s (%s-%s)" % (self.seccion.curso.colegio.nombre, self.seccion.curso.nombre, self.seccion.nombre, self.desde.year, self.hasta.year)
    class Meta:
        ordering = ['-desde']

class HorarioDia(models.Model):
    horario = models.ForeignKey(Horario)
    dia = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    def __unicode__(self):
        descDia=[ y for x, y in DAYS_OF_WEEK if int(x)  == int(self.dia)][0]
        return u"%s: %s" % (self.horario, descDia)
    class Meta:
        ordering = ['dia']

class HorarioDetalle(models.Model):
    horariodia = models.ForeignKey(HorarioDia)
    desde = models.TimeField()
    hasta = models.TimeField()
    materia = models.ForeignKey(Materia)
