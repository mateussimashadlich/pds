from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from exercito.models import Pais, Batalhao, Exercito, Militar, Pessoa


@api_view(['GET', 'POST'])
def paises(request):
    if request.method == 'GET':
        paises = [model_to_dict(pais) for pais in Pais.objects.all()]
        return Response(paises)
    elif request.method == 'POST':
        try:
            pais = Pais(
                nome=request.data['nome'],
                continente=request.data['continente'],
                tamanho=request.data['tamanho'],
            )
            pais.save()
            return Response(model_to_dict(pais), status=201)

        except Exception as e:
            return Response({'message': 'Dados inválidos.'}, status=400)


@api_view(['GET'])
def pais(request, id):
    pais = Pais.objects.get(id=id)
    return Response(model_to_dict(pais))


@api_view(['GET'])
def continentes(request):
    continentes = [
        {'valor': continente[0], 'nome': continente[1]} for continente in Pais.CONTINENTES
    ]
    return Response(continentes)


@api_view(['GET', 'POST'])
def batalhoes(request):
    if request.method == 'GET':
        batalhoes = [model_to_dict(batalhao) for batalhao in Batalhao.objects.all()]
        return Response(batalhoes)

    elif request.method == 'POST':
        try:
            exercito = Exercito.objects.get(pk=request.data['exercito'])
            comandante = Militar.objects.get(pk=request.data['comandante'])
            batalhao = Batalhao(
                nome=request.data['nome'],
                exercito=exercito,
                comandante=comandante,
            )
            batalhao.save()
            return Response(model_to_dict(batalhao), status=201)

        except Exception as e:
            return Response({'message': 'Dados inválidos.'}, status=400)


@api_view(['GET'])
def batalhao(request, id):
    batalhao = Batalhao.objects.get(id=id)
    return Response(model_to_dict(batalhao))


@api_view(['GET', 'POST'])
def exercitos(request):
    if request.method == 'GET':
        exercitos = [model_to_dict(exercito) for exercito in Exercito.objects.all()]
        return Response(exercitos)

    elif request.method == 'POST':
        try:
            pais = Pais.objects.get(pk=request.data['pais'])
            exercito = Exercito(
                pais=pais,
                lema=request.data['lema'],
                ano_fundacao=request.data['ano_fundacao'],
            )
            exercito.save()
            return Response(model_to_dict(exercito), status=201)

        except Exception as e:
            return Response({'message': 'Dados inválidos.'}, status=400)


@api_view(['GET', 'POST'])
def militares(request):
    if request.method == 'GET':
        militares = [model_to_dict(militar) for militar in Militar.objects.all()]
        return Response(militares)

    elif request.method == 'POST':
        try:
            pessoa = Pessoa.objects.get(pk=request.data['pessoa'])
            batalhao_atual = None
            if request.data['batalhao_atual']:
                batalhao_atual = Batalhao.objects.get(pk=request.data['batalhao_atual'])
                
            militar = Militar(
                pessoa=pessoa,
                batalhao_atual=batalhao_atual,
                patente=request.data['patente'],
                ano_ingresso=request.data['ano_ingresso'],
            )
            militar.save()
            return Response(model_to_dict(militar), status=201)

        except Exception as e:
            raise Exception(e)
            return Response({'message': 'Dados inválidos.'}, status=400)


@api_view(['GET'])
def patentes(request):
    patentes = [{'valor': patente[0], 'nome': patente[1]} for patente in Militar.PATENTES]
    return Response(patentes)


@api_view(['GET', 'POST'])
def pessoas(request):
    if request.method == 'GET':
        pessoas = [model_to_dict(pessoa) for pessoa in Pessoa.objects.all()]
        return Response(pessoas)

    elif request.method == 'POST':
        try:
            pessoa = Pessoa(
                nome=request.data['nome'],
                idade=request.data['idade'],
                peso=request.data['peso'],
                altura=request.data['altura'],
            )
            pessoa.save()
            return Response(model_to_dict(pessoa), status=201)

        except Exception as e:
            return Response({'message': 'Dados inválidos.'}, status=400)


@api_view(['GET'])
def pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return Response(model_to_dict(pessoa))


@api_view(['GET'])
def pessoas_nao_militares(request):
    id_pessoas_militares = Militar.objects.all().values('id')
    pessoas_nao_militares = Pessoa.objects.exclude(id__in=id_pessoas_militares)
    return Response([model_to_dict(pessoa) for pessoa in pessoas_nao_militares])