import datetime

from ..models import Exercito

exercitos = [
    Exercito(lema='Braço forte, mão amiga', ano_fundacao=datetime.date(1822, 1, 1)),
    Exercito(lema='Forward', ano_fundacao=datetime.date(1962, 7, 31)),
    Exercito(lema="This we'll defend", ano_fundacao=datetime.date(1775, 6, 14)),
]
