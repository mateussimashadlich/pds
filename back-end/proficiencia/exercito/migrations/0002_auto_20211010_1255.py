# def combine_names(apps, schema_editor):
#     # We can't import the Person model directly as it may be a newer
#     # version than this migration expects. We use the historical version.
#     Person = apps.get_model('yourappname', 'Person')
#     for person in Person.objects.all():
#         person.name = '%s %s' % (person.first_name, person.last_name)
#         person.save()

# class Migration(migrations.Migration):

#     dependencies = [
#         ('yourappname', '0001_initial'),
#     ]

#     operations = [
#         migrations.RunPython(combine_names),
#     ]


# Generated by Django 3.2 on 2021-10-10 15:55

from django.db import migrations
from ..models import Pais, Pessoa

from ..dados_iniciais.pais import paises
from ..dados_iniciais.militar import militares
from ..dados_iniciais.pessoa import pessoas
from ..dados_iniciais.exercito import exercitos

# from dados_inicias_batalhao import batalhoes


def popular_pais(apps, schema_editor):
    """Popula a entidade Pais com alguns dados iniciais"""
    for pais in paises:
        pais.save()


def popular_militar(apps, schema_editor):
    """Popula a entidade Militar com alguns dados iniciais"""
    for militar in militares:
        pessoa = Pessoa.objects.get(pk=militares.index(militar)+1)
        militar.pessoa = pessoa
        militar.save()

def popular_pessoa(apps, schema_editor):
    """Popula a entidade Pessoa com alguns dados iniciais"""
    for pessoa in pessoas:        
        pessoa.save()


def popular_exercito(apps, schema_editor):
    """Popula a entidade Exercito com alguns dados iniciais"""
    for exercito in exercitos:
        pais = Pais.objects.get(pk=exercitos.index(exercito)+1)
        exercito.pais = pais
        exercito.save()


def popular_batalhao(apps, schema_editor):
    """Popula a entidade Batalhao com alguns dados iniciais"""
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('exercito', '0001_initial')
    ]

    operations = [
        migrations.RunPython(popular_pais),
        migrations.RunPython(popular_pessoa),
        migrations.RunPython(popular_militar),
        migrations.RunPython(popular_exercito),        
    ]
