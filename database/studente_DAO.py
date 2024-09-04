# Importare il metodo get_connection dal file DB_connect della cartella Python database
from database.DB_connect import get_connection

# Importare la classe Studente dal modulo studente della cartella Python model
from model.studente import Studente

# Definire una funzione cerca_studente: dato il numero di matricola, ne viene restituito lo studente corrispondente a
# tale matricola
def cerca_studente(numero_di_matricola):
    # Creare una connessione con il database
    cnx = get_connection()
    # Se la connessione è avvenuta correttamente,...
    if cnx is not None:
        # Creare il cursore
        cursor = cnx.cursor(dictionary = True)
        # Creare la query che verrà eseguita
        query = """select * from studente s where s.matricola = %s"""
        # Eseguire la query tramite l'apposita funzione del cursore
        cursor.execute(query, (numero_di_matricola,)) # si scrive così perché non può essere una semplice stringa, ma bensì
        # deve essere una tupla, una lista o un dizionario
        # Essendo la matricola unica per ogni studente, il database troverà solo una riga
        row = cursor.fetchone()
        # Se la riga non esiste,...
        if row is None:
            # Non esiste un studente corrispondente a quella riga
            studente = None
        # Altrimenti...
        else:
            # Creare l'oggetto studente
            studente = Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
        # Chiudere il cursore e la connessione
        cursor.close()
        cnx.close()
        # Restituire il risultato
        return studente
    # Se la connessione non fosse avvenuta correttamente, allora verrà visualizzato il seguente messaggio
    else:
        print("C'è stato un problema nel creare la connessione")
