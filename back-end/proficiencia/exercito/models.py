from django.db import models


class Pais(models.Model):
    CONTINENTES = [
        ('AMS', 'América do Sul'),
        ('AMC', 'América Central'),
        ('AMN', 'América do Norte'),
        ('AFR', 'África'),
        ('EUR', 'Europa'),
        ('ASI', 'Ásia'),
        ('OCE', 'Oceania'),
    ]

    nome = models.CharField(max_length=255, unique=True)
    continente = models.CharField(max_length=3, choices=CONTINENTES)
    tamanho = models.FloatField()
    
    def __str__(self):
        return self.nome


class Exercito(models.Model):
    pais = models.OneToOneField(Pais, on_delete=models.CASCADE, unique=True, verbose_name='País')
    lema = models.CharField(max_length=255)
    ano_fundacao = models.DateField()


class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    peso = models.DecimalField(max_digits=3, decimal_places=0)
    altura = models.DecimalField(max_digits=3, decimal_places=0)


class Militar(models.Model):
    PATENTES = [
        ('SOL', 'Soldado'),
        ('CAB', 'Cabo'),
        ('SAR', 'Sargento'),
        ('SUB', 'Subtenente'),
        ('TEN', 'Tenente'),
        ('CAP', 'Capitão'),
        ('MAJ', 'Major'),
        ('COR', 'Coronel'),
        ('GEN', 'General'),
    ]

    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    patente = models.CharField(max_length=255, choices=PATENTES)
    batalhao_atual = models.ForeignKey(
        'Batalhao', on_delete=models.PROTECT, null=True, verbose_name='Batalhão'
    )
    ano_ingresso = models.DateField('Ano de Ingresso')


class Batalhao(models.Model):
    nome = models.CharField(max_length=255)
    exercito = models.ForeignKey(Exercito, on_delete=models.CASCADE, verbose_name='Exército')
    comandante = models.ForeignKey('Militar', on_delete=models.PROTECT)
