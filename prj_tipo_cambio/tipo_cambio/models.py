from django.db import models

class TipoDeCambio(models.Model):

    cambio = models.DecimalField(decimal_places=5, max_digits=10)
    fecha = models.DateField(unique=True, error_messages={"unique":"Fecha duplicada."})

    def to_row(self):
        return f'<tr><td>{self.id}</td><td>{self.fecha}</td><td>{self.cambio}</td><td><a href="../update/{self.id}">Editar</a> / <a href="../delete/{self.id}">Borrar</a></td></tr>'