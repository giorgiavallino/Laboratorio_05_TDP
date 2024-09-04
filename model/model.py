# Importare il modulo corso_DAO
from database import corso_DAO

# Importare il modulo studente_DAO
from database import studente_DAO

# Creare la classe Model
class Model:

    # Creare il metodo add_corsi che restituisce il metodo add_corsi creato nel file corso_DAO della cartella Python
    # database
    def add_corsi(self):
        return corso_DAO.add_corsi()

    # Creare il metodo cerca_iscritti che restituisce il metodo cerca_iscritti creato nel file corso_DAO della cartella
    # Python database
    def cerca_iscritti(self, codice_corso):
        return corso_DAO.cerca_iscritti(codice_corso)

    # Creare il metodo cerca_studente che restituisce il metodo cerca_studente creato nel file studente_DAO della
    # cartella Python database
    def cerca_studente(self, numero_di_matricola):
        return studente_DAO.cerca_studente(numero_di_matricola)

    # Creare il metodo cerca_corsi che restituisce il metodo cerca_corsi creato nel file corso_DAO della cartella
    # Python database
    def cerca_corsi(self, numero_di_matricola):
        return corso_DAO.cerca_corsi(numero_di_matricola)

    def iscrivi(self, numero_di_matricola, codice_corso):
        return corso_DAO.iscrivi(numero_di_matricola, codice_corso)