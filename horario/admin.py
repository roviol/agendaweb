from django.contrib import admin

# Register your models here.

from horario.models import Pais
from horario.models import Ciudad
from horario.models import Colegio
from horario.models import Curso
from horario.models import Seccion
from horario.models import Materia
from horario.models import MateriaCurso
from horario.models import Horario
from horario.models import HorarioDia
from horario.models import HorarioDetalle

class ColegioInline(admin.TabularInline):
    model = Colegio
    extra = 1

class CiudadAdmin(admin.ModelAdmin):
    inlines = [ColegioInline]


class HorarioDiaInline(admin.TabularInline):
    model = HorarioDia
    extra = 1

class HorarioAdmin(admin.ModelAdmin):
    inlines = [HorarioDiaInline]


class HorarioDetalleInline(admin.TabularInline):
    model = HorarioDetalle
    extra = 1

class HorarioDiaAdmin(admin.ModelAdmin):
    inlines = [HorarioDetalleInline]

admin.site.register(Pais)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Curso)
admin.site.register(Seccion)
admin.site.register(Materia)
admin.site.register(MateriaCurso)
admin.site.register(Horario,HorarioAdmin)
admin.site.register(HorarioDia,HorarioDiaAdmin)
admin.site.register(HorarioDetalle)
