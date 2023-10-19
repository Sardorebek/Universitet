from django.db import models

JINS = [
    ("Erkak","Erkak"),
    ("Ayol","Ayol")
]

DARAJA =[
    ("Bakalavr","Bakalavr"),
    ("Magistr","Magistr")
]
class Yonalish(models.Model):
    nom = models.CharField(max_length=30)
    aktiv = models.BooleanField(blank=True)

    def __str__(self):
        return f"{self.nom}"

class Fan(models.Model):
    nom = models.CharField(max_length=40)
    yonalish = models.OneToOneField(Yonalish, on_delete=models.CASCADE)
    asosiy = models.BooleanField(blank=True)

    def __str__(self):
        return f"{self.yonalish}"

class Ustoz(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.PositiveSmallIntegerField()
    jins = models.CharField(max_length=6,choices=JINS)
    daraja = models.CharField(max_length=10,choices=DARAJA)
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ism}"