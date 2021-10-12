import decimal
from ..models import Pessoa

pessoas = [
    Pessoa(
        nome='João Antibes Donatello',
        idade=50,
        peso=decimal.Decimal('71'),
        altura=decimal.Decimal('178'),
    ),
    Pessoa(
        nome='Maria Carvalho',
        idade=65,
        peso=decimal.Decimal('61'),
        altura=decimal.Decimal('170'),
    ),
    Pessoa(
        nome='Júlio César', idade=45, peso=decimal.Decimal('80'), altura=decimal.Decimal('180')
    ),
    Pessoa(
        nome='Cassiano Torquato', idade=28, peso=decimal.Decimal('70'), altura=decimal.Decimal('170')
    ),
]
