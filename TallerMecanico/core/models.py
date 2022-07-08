from django.db import models

# Create your models here.

class Categorias(models.Model):
  idCategoria = models.IntegerField(primary_key = True, verbose_name = 'Id de categoria')
  nombreCategoria = models.CharField(max_length = 50, verbose_name = 'Nombre de la cetgoria')

  def __str__(self):
    return self.nombreCategoria

class Contacto(models.Model):
  rut = models.CharField(max_length = 10, primary_key = True, verbose_name = 'Rut')
  nombre = models.CharField(max_length = 40, verbose_name = 'Nombre')
  correo = models.CharField (max_length = 20, verbose_name = 'Correo')
  mensaje = models.CharField (max_length = 100, null = True, blank = True, verbose_name = 'Mensaje')
  categoria = models.ForeignKey(Categorias, on_delete = models.CASCADE)

  def __str__(self):
    return self.rut


class Trabajo(models.Model):
  diagnostico = models.CharField(max_length = 200, verbose_name = 'Diagnostico')
  mecanico =models.CharField(max_length= 50, verbose_name='Mecanico')
  fecha = models.DateField(max_length=9, verbose_name='Fecha')
  materiales = models.CharField(max_length=200, verbose_name='Materiales')
  img = models.ImageField(null = True, blank = True)
  categoria = models.ForeignKey(Categorias, on_delete = models.CASCADE)
  

  def __str__(self):
    return self.mecanico
  

