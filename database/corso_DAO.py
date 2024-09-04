# Add whatever it is needed to interface with the DB Table corso

# Importare la connessione al database
from database.DB_connect import get_connection

# Importare la classe corso del modello
from model.corso import Corso

# Importare la classe studente dal modello
from model.studente import Studente

# Creare la funzione add_corsi() per aggiungere alla dropdown i relativi corsi
def add_corsi() -> list[Corso] | None:
    # Creare una connessione con il database
    cnx = get_connection()
    # Creare una variabile result in cui verranno appesi i risultati qualora la connessione fosse avvenuta
    result = []
    # Se la connessione è avvenuta correttamente,...
    if cnx is not None:
        # Creare il cursore
        cursor = cnx.cursor(dictionary = True)
        # Creare la query che verrà eseguita
        query = """SELECT * FROM corso"""
        # Eseguire la query tramite l'apposita funzione del cursore
        cursor.execute(query)
        # Vengono lette tutte le righe del database
        rows = cursor.fetchall()
        # Per ogni riga...
        for row in rows:
            # Creare un oggetto corso costituto dalle variabili richieste, ossia codins, crediti, nome e pd
            corso = Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
            # Appendere i corsi alla lista result: in questo modo, si avrà una lista costituita da oggetti di tipo
            # Corso... più semplicemente si avrà una lista contenente ciascun corso con le relative proprietà
            result.append(corso)
        # Chiudere il cursore e la connessione
        cursor.close()
        cnx.close()
        # Restituire la variabile result
        return result
    # Se la connessione non fosse avvenuta correttamente, allora verrà visualizzato il seguente messaggio
    else:
      print("C'è stato un problema nel creare la connessione")

# Definire la funzione cerca_iscritti, la quale dato un codice di un corso ne trova i relativi iscritti
def cerca_iscritti(codice_corso):
    # Creare una connessione con il database
    cnx = get_connection()
    # Creare una variabile result in cui verranno appesi i risultati qualora la connessione fosse avvenuta
    result = []
    # Se la connessione è avvenuta correttamente,...
    if cnx is not None:
        # Creare il cursore
        cursor = cnx.cursor(dictionary = True)
        # Creare la query che verrà eseguita
        query = """select * from studente s, iscrizione i where s.matricola = i.matricola and i.codins = %s"""
        # Eseguire la query tramite l'apposita funzione del cursore
        cursor.execute(query, (codice_corso,)) # si scrive così perché non può essere una semplice stringa, ma bensì
        # deve essere una tupla, una lista o un dizionario
        # Leggere le righe create/trovate mediante la query
        rows = cursor.fetchall()
        # Per ogni riga...
        for row in rows:
            # Creare l'oggetto studente
            studente = Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
            # Appendere l'oggetto studente al risultato
            result.append(studente)
        # Chiudere il cursore e la connessione
        cursor.close()
        cnx.close()
        # Restituire il risultato
        return result
    # Se la connessione non fosse avvenuta correttamente, allora verrà visualizzato il seguente messaggio
    else:
        print("C'è stato un problema nel creare la connessione")

def cerca_corsi(numero_di_matricola):
    result = []
    # Creare una connessione con il database
    cnx = get_connection()
    # Se la connessione è avvenuta correttamente,...
    if cnx is not None:
        # Creare il cursore
        cursor = cnx.cursor(dictionary=True)
        # Creare la query che verrà eseguita
        query = """select * from studente s, corso c, iscrizione i 
        where s.matricola = i.matricola and c.codins = i.codins and s.matricola = %s"""
        # Eseguire la query tramite l'apposita funzione del cursore
        cursor.execute(query,
                       (numero_di_matricola,))  # si scrive così perché non può essere una semplice stringa, ma bensì
        # deve essere una tupla, una lista o un dizionario
        # Essendo la matricola unica per ogni studente, il database troverà solo una riga
        row = cursor.fetchone()
        # Se la riga non esiste,...
        if row is None:
            # Non esiste un studente corrispondente a quella matricola
            studente = None
        # Altrimenti...
        else:
            # Creare l'oggetto studente
            studente = Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
            # Creare l'oggetto corso_01
            corso_01 = Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
            # Appendere l'oggetto corso_01 alla lista result
            result.append(corso_01)
        # Leggere le righe rimanenti
        rows_remaining = cursor.fetchall()
        # Per ogni riga...
        for row in rows_remaining:
            # Inizializzare la variabile corso_02
            corso_02 = Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
            # Appendere la variabile appena creata alla lista result
            result.append(corso_02)
        # Chiudere il cursore e la connessione
        cursor.close()
        cnx.close()
        # Restituire il risultato
        return studente, result
        # Se la connessione non fosse avvenuta correttamente, allora verrà visualizzato il seguente messaggio
    else:
        print("C'è stato un problema nel creare la connessione")

def iscrivi(numero_di_matricola, codice_corso):
    # Creare una connessione con il database
    cnx = get_connection()
    # Inizializzare la variabile result
    result = None
    # Creare la query che verrà eseguita
    query = """INSERT IGNORE INTO iscrizione (matricola, codins) VALUES (%s, %s)"""
    # Se la connessione è avvenuta correttamente,...
    if cnx is not None:
        # Creare il cursore
        cursor = cnx.cursor()
        # Eseguire la query tramite l'apposita funzione del cursore
        cursor.execute(query,
                       (numero_di_matricola, codice_corso,))
        # Fare il commit
        cnx.commit()
        # Chiudere il cursore e la connessione
        cursor.close()
        cnx.close()
        # Restituire True
        result = True
        return result
    # Se la connessione non fosse avvenuta correttamente, allora verrà visualizzato il seguente messaggio
    else:
        print("C'è stato un problema nel creare la connessione")
        # Restituire False
        result = False
        return result