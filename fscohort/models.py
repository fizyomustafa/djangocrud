from django.db import models

class Student(models.Model):
    img = models.ImageField(verbose_name= "Resim Yükle", null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Öğrenci"
        verbose_name_plural = "Öğrenciler"
        ordering = ['number']