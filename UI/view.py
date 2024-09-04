# Importare il modulo flet, come ft, che sarà utilizzato in seguito
import flet as ft

# Creare una classe View
class View(ft.UserControl):

    # Definire un metodo __init__ che contenga tutti gli elementi grafici che saranno utilizzati per creare l'omonima
    # interfaccia grafica
    def __init__(self, page: ft.Page):
        super().__init__()
        # Elementi grafici relativi alla pagina
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self._controller = None
        # Elementi grafici
        self._title = None
        self.dd_corsi = None
        self.btn_cerca_iscritti = None
        self.txt_matricola = None
        self.txt_nome = None
        self.txt_cognome = None
        self.btn_cerca_studente = None
        self.btn_cerca_corsi = None
        self.btn_iscrivi = None
        self.lv_result = None

    # Definire un metodo load_interface che gestisca e introduca gli elementi grafici dell'interfaccia grafica (ossia
    # della view)
    def load_interface(self):

        # Titolo
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.add(self._title)

        # Row 1
        self.dd_corsi = ft.Dropdown(label = "Corso",
                                    options = [],
                                    hint_text = "Scegliere il corso",
                                    width = 550)
        self._controller.add_options()
        self.btn_cerca_iscritti = ft.ElevatedButton(text = "Cerca iscritti",
                                                    on_click = self._controller.cerca_iscritti,
                                                    tooltip = "Cerca gli iscritti del corso selezionato")
        row_01 = ft.Row([self.dd_corsi, self.btn_cerca_iscritti],
                        alignment = ft.MainAxisAlignment.CENTER)
        self._page.add(row_01)

        # Row 2
        self.txt_matricola = ft.TextField(label = "Matricola",
                                          hint_text = "Inserire il numero di matricola",
                                          width = 150)
        self.txt_nome = ft.TextField(label = "Nome",
                                     hint_text = "Inserire il nome dello studente",
                                     read_only = True,
                                     width = 300)
        self.txt_cognome = ft.TextField(label = "Cognome",
                                     hint_text = "Inserire il cognome dello studente",
                                     read_only = True,
                                     width = 300)
        row_02 = ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome],
                        alignment = ft.MainAxisAlignment.CENTER)
        self._page.add(row_02)

        # Row 3
        self.btn_cerca_studente = ft.ElevatedButton(text = "Cerca studente",
                                                    on_click = self._controller.cerca_studente,
                                                    tooltip = "Cerca l'esistenza di uno studente con la matricola inserita")
        self.btn_cerca_corsi = ft.ElevatedButton(text = "Cerca corsi",
                                                 on_click = self._controller.cerca_corsi,
                                                 tooltip = "Cerca i corsi a cui è iscritta la matricola inserita")
        self.btn_iscrivi = ft.ElevatedButton(text = "Iscrivi",
                                             on_click = self._controller.iscrivi,
                                             tooltip = "Iscrivi la matricola inserita al corso selezionato")
        row_03 = ft.Row([self.btn_cerca_studente, self.btn_cerca_corsi, self.btn_iscrivi],
                        alignment = ft.MainAxisAlignment.CENTER)
        self._page.add(row_03)

        # List View
        self.lv_result = ft.ListView(expand = 1,
                                     spacing = 10,
                                     padding = 20,
                                     auto_scroll = True)
        self._page.add(self.lv_result)
        self._page.update()

    # Definire il metodo set_controller per impostare il controller nella view
    def set_controller(self, controller):
        self._controller = controller

    # Definire il metodo create_alert, il quale crea un avviso con il corrispondente messaggio ogni volta venga
    # utilizzato
    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    # Definire il metodo update_page, il quale permette di scrivere update_page al posto di ._page update ogni qual
    # volta venga aggiornata la pagina per inserire o aggiornare gli elementi grafici
    def update_page(self):
        self._page.update()