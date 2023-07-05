from django.db import models

class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=45)
    tugilgan_yil = models.DateField()
    davlat = models.CharField(max_length=45)
    def __str__(self):
        return self.ism

class Albom(models.Model):
    nom = models.CharField(max_length=75)
    sana = models.DateField()
    rasm = models.URLField(null=True)
    qoshiqchi=models.ForeignKey(Qoshiqchi,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Qoshiq(models.Model):
    nom = models.CharField(max_length=65)
    janr = models.CharField(max_length=60)
    davomiylik = models.DurationField(null=True)
    fayl = models.TextField(null=True)
    albom = models.ForeignKey(Albom,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom





