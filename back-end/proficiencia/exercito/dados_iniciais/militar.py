from ..models import Militar
import datetime

militares = [
    Militar(patente='COR', ano_ingresso=datetime.date(1991, 7, 1)),
    Militar(patente='GEN', ano_ingresso=datetime.date(1980, 9, 11)),
    Militar(patente='CAP', ano_ingresso=datetime.date(1999, 7, 1)),
]
