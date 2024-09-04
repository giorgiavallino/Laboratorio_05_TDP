# Importare il modulo flet come ft
import flet as ft

# Creare la classe Controller
class Controller:

    # Definire il metodo __init__
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    # Definire il metodo add_options che aggiunge le opzioni al dropdown che è stato creato nella view
    def add_options(self):
        # Inizializzare la variabile corsi che crea una lista contente i corsi del database
        corsi = self._model.add_corsi()
        # Per ogni elemento della lista, viene aggiunta la relativa opzione nella dropdown
        for corso in corsi:
            self._view.dd_corsi.options.append(ft.dropdown.Option(key = corso.codins, text = corso.__str__()))
        # Fare l'update della pagina
        self._view.update_page()

    # Definire il metodo cerca_iscritti, il quale per il corso selezionato restituisce gli studenti (compresi di nome,
    # cognome e numero di matricola) iscritti
    def cerca_iscritti(self, e):
        # Definire la variabile corso, che rappresenta il valore selezionato nel menù a tendina
        self.corso = self._view.dd_corsi.value # viene restituito il codice del corso
        # Se il corso non è stato selezionato, allora viene scritto un messaggio di avviso segnalando che l'operazione
        # non può essere proseguita a causa della mancanza del valore richiesto
        if self.corso is None:
            self._view.create_alert("Inserire un corso per proseguire l'operazione!")
            self._view.update_page()
        # Altrimenti, si prosegue con le operazioni: per ogni studente iscritto viene aggiunta una riga di testo alla
        # list view con i relativi dati richiesti
        else:
            # Eliminare i precedenti elementi testuali aggiunti alla list view in maniera tale da avere una
            # comprensione più semplice di quanto voluto
            self._view.lv_result.controls.clear()
            # Inizializzare studenti
            studenti = self._model.cerca_iscritti(self.corso)
            # Se ci sono degli studenti, verranno stampati i relativi valori nella list_view
            if len(studenti) > 0:
                self._view.lv_result.controls.append(ft.Text(f"Ci sono {len(studenti)} iscritti."))
                for studente in studenti:
                    self._view.lv_result.controls.append(ft.Text(studente.__str__()))
                self._view.update_page()
            # Altrimenti, verrà stampato nella list view un messaggio nel quale viene detto che non sono presenti
            # iscritti per il corso selezionato
            elif len(studenti) == 0:
                self._view.lv_result.controls.append(ft.Text("Non ci sono iscritti."))
                self._view.update_page()

    # Definire il metodo cerca_studente, il quale cerca per la matricola inserita i relativi dati dello studente, ossia
    # nome e cognome
    def cerca_studente(self, e):
        # Inizializzare la variabile matricola che corrisponde al valore numerico inserito all'interno dell'apposito
        # text field
        matricola = self._view.txt_matricola.value
        # Se non è stata inserita la matricola, allora verrà visualizzato il corrispondente messaggio di avviso
        if matricola == "":
            self._view.create_alert("Inserire il numero di matricola dello studente per proseguire l'operazione!")
            self._view.update_page()
        # Se la matricola è stata inserita correttamente,...
        else:
            # Eliminare i precedenti valori testuali inseriti nella list view
            self._view.lv_result.controls.clear()
            # Inizializzare i valori del nome e del cognome disposti in separate text field come None
            self._view.txt_nome.value = None
            self._view.txt_cognome.value = None
            # Inizializzare la variabile studente
            studente = self._model.cerca_studente(matricola)
            # Se la ricerca dello studente è fallita in quanto è stato utilizzato un numero di matricola sbagliato,
            # allora verrà visualizzato un messaggio che indica la fallita corrispondeza matricola-studente
            if studente is None:
                self._view.lv_result.controls.append(ft.Text("Non esiste uno studente con la matricola ricercata."))
                self._view.update_page()
            # Se la ricerca è andata a buon fine, allora il valore delle text field nome e cognome sarà aggiornato e
            # corrisponderà al nome e al cognome dello studente avente la matricola inserita
            else:
                self._view.txt_nome.value = studente.nome
                self._view.txt_cognome.value = studente.cognome
                self._view.update_page()

    # Definire il metodo cerca_corsi, il quale cerca inserita la matricola di uno studente i corsi a cui è iscritto
    def cerca_corsi(self, e):
        # Inizializzare la variabile matricola che corrisponde al valore numerico inserito all'interno dell'apposito
        # text field
        matricola = self._view.txt_matricola.value
        # Se non è stata inserita la matricola, allora verrà visualizzato il corrispondente messaggio di avviso
        if matricola == "":
            self._view.create_alert("Inserire il numero di matricola dello studente per proseguire l'operazione!")
            self._view.update_page()
        # Se la matricola è stata inserita correttamente,...
        else:
            # Eliminare i precedenti valori testuali inseriti nella list view
            self._view.lv_result.controls.clear()
            # Inizializzare i valori del nome e del cognome disposti in separate text field come None
            self._view.txt_nome.value = None
            self._view.txt_cognome.value = None
            # Inizializzare la variabile studente e corsi
            studente, corsi = self._model.cerca_corsi(matricola)
            # Se la ricerca dello studente è fallita in quanto è stato utilizzato un numero di matricola sbagliato,
            # allora verrà visualizzato un messaggio che indica la fallita corrispondeza matricola-studente
            if studente is None:
                self._view.lv_result.controls.append(ft.Text("Non esiste uno studente con la matricola ricercata."))
                self._view.update_page()
            # Se la ricerca è andata a buon fine, allora verranno stampati i corsi a cui è iscritta la matricola
            # inserita
            else:
                self._view.lv_result.controls.append(ft.Text(f"Risultano {len(corsi)} corsi: "))
                for corso in corsi:
                    self._view.lv_result.controls.append(ft.Text(f"{corso.nome}"))
                self._view.update_page()

    # Definire il metodo iscrivi, il quale iscrivi uno studente a un determinati corso
    def iscrivi(self, e):
        # Inizializzare la variabile matricola che corrisponde al valore numerico inserito all'interno dell'apposito
        # text field
        matricola = int(self._view.txt_matricola.value)
        # Se non è stata inserita la matricola, allora verrà visualizzato il corrispondente messaggio di avviso
        if matricola == "":
            self._view.create_alert("Inserire il numero di matricola dello studente per proseguire l'operazione!")
            return
        # Definire la variabile corso, che rappresenta il valore selezionato nel menù a tendina
        codice_corso = self._view.dd_corsi.value  # viene restituito il codice del corso
        # Se il corso non è stato selezionato, allora viene scritto un messaggio di avviso segnalando che l'operazione
        # non può essere proseguita a causa della mancanza del valore richiesto
        if codice_corso is None:
            self._view.create_alert("Inserire un corso per proseguire l'operazione!")
            return
        # Inizializzare la variabile studente
        studente = self._model.cerca_studente(matricola)
        # Se la ricerca dello studente è fallita in quanto è stato utilizzato un numero di matricola sbagliato,
        # allora verrà visualizzato un messaggio che indica la fallita corrispondeza matricola-studente
        if studente is None:
            self._view.lv_result.controls.append(ft.Text("Non esiste uno studente con la matricola ricercata."))
            return
        result = self._model.iscrivi(codice_corso, matricola)
        self._view.lv_result.controls.clear()
        if result == True:
            self._view.lv_result.controls.append(ft.Text(f"Iscrizione effettuata con successo!"))
        else:
            self._view.lv_result.controls.append(ft.Text(f"Iscrizione non effettuata!"))
        self._view.update_page()