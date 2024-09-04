# Importare dal modulo dataclasses la funzione dataclass
from dataclasses import dataclass

# Definire una classe Studente attraverso la funzione dataclass
@dataclass
class Studente:
    matricola: int
    cognome: str
    nome: str
    CDS: str

    # Definire una funzione __str__, che restituisce il nome e il cognome dello studente mettendo al fondo tra parentesi
    # il numero di matricola
    def __str__(self):
        return f"{self.nome}, {self.cognome} ({self.matricola})"

    # Definire una funzione __eq__
    def __eq__(self, other):
        return self.matricola == other.matricola