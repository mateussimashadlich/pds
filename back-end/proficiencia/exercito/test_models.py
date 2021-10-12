import datetime

from django.test import TestCase
from exercito.models import Batalhao, Exercito, Militar, Pais, Pessoa


class BasicTestCase(TestCase):
    def setUp(self):
        self.pais = Pais.objects.create(nome='Argentina', continente='AMS', tamanho=1234567)
        self.exercito = Exercito.objects.create(pais=self.pais, lema='Bla', ano_fundacao=datetime.date(1800, 10, 10))
        self.pessoa = Pessoa.objects.create(nome="João", idade=21, peso=100, altura=200)
        self.militar = Militar.objects.create(pessoa=self.pessoa, patente='SOL', batalhao_atual=None, ano_ingresso=datetime.date(1999, 10, 10))
        self.batalhao = Batalhao.objects.create(nome='11º Batalhão de Infantaria', exercito=self.exercito, comandante=self.militar)
    
    def test_pais_str(self):
        self.assertEqual(str(self.pais), self.pais.nome)    