from django.db import models



class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.nome

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    ano_lancamento = models.DateField(blank=True, null=True)
    valor = models.DecimalField(decimal_places=2, max_digits=15, blank=True, null=True)
    placa = models.CharField(max_length=7, blank=True, null=True)
    imagens_veiculos = models.ImageField(upload_to='App', blank=True, null=True)

    class Meta:
        verbose_name = 'Carro'


    def __str__(self):
        return self.modelo
