# Importare la funzione dataclass dal modulo dataclasses
from dataclasses import dataclass

# Creare la classe Corso attraverso la funzione @dataclass inserendo come variabili le rispettive colonne dell'
# omonima tabella del database
@dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int

    # Definire il metodo __eq__
    def __eq__(self, other):
        return self.codins == other.codins

    # Definire il metodo __hash__
    def __hash__(self):
        return hash(self.codins)

    # Definire il metodo str
    def __str__(self):
        return f'{self.nome} ({self.codins})'