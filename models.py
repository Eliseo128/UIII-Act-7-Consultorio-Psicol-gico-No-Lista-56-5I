from django.db import models

class PacientePsicologia(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    ocupacion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    motivo_consulta = models.TextField()
    historial_psicologico = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Psicologo(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    licencia_profesional = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    enfoque_terapeutico = models.CharField(max_length=100)
    salario_hora = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class SesionTerapia(models.Model):
    paciente = models.ForeignKey(PacientePsicologia, on_delete=models.CASCADE)
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    fecha_sesion = models.DateField()
    hora_inicio = models.TimeField()
    duracion_minutos = models.IntegerField()
    tipo_sesion = models.CharField(max_length=50)
    objetivos_sesion = models.TextField()
    notas_terapeuta = models.TextField()
    tareas_asignadas = models.TextField()

    def __str__(self):
        return f"Sesión {self.id} - {self.fecha_sesion}"


class Diagnostico(models.Model):
    paciente = models.ForeignKey(PacientePsicologia, on_delete=models.CASCADE)
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    fecha_diagnostico = models.DateField()
    codigo_cie10 = models.CharField(max_length=20)
    descripcion_diagnostico = models.TextField()
    severidad = models.CharField(max_length=50)
    plan_tratamiento = models.TextField()
    pronostico = models.CharField(max_length=100)

    def __str__(self):
        return f"Diagnóstico {self.codigo_cie10} - {self.paciente.nombre}"


class Terapia(models.Model):
    nombre_terapia = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_estimada_sesiones = models.IntegerField()
    enfoque_terapeutico = models.CharField(max_length=100)
    indicaciones = models.TextField()
    contraindicaciones = models.TextField()
    efectividad_porcentaje = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre_terapia


class EvaluacionPsicologica(models.Model):
    paciente = models.ForeignKey(PacientePsicologia, on_delete=models.CASCADE)
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    fecha_evaluacion = models.DateField()
    tipo_prueba = models.CharField(max_length=100)
    resultados_cuantitativos = models.TextField()
    interpretacion = models.TextField()
    recomendaciones = models.TextField()
    fecha_proxima_evaluacion = models.DateField()

    def __str__(self):
        return f"Evaluación {self.id} - {self.paciente.nombre}"


class FacturaPsicologia(models.Model):
    paciente = models.ForeignKey(PacientePsicologia, on_delete=models.CASCADE)
    fecha_emision = models.DateField()
    concepto_servicios = models.TextField()
    subtotal_sesiones = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    total_factura = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)
    sesiones_cubiertas = models.IntegerField()

    def __str__(self):
        return f"Factura {self.id} - {self.paciente.nombre}"
