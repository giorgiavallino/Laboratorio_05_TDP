# Importare la libreria flet come ft
import flet as ft

# Importare vari moduli e classi dai file del progetto che verranno utilizzati per costruire il main dell'applicazione
from model.model import Model
from UI.view import View
from UI.controller import Controller

# Definire il main, che sarà costituito dal modello, dalla view e dal controller
def main(page: ft.Page):
    my_model = Model()
    my_view = View(page)
    my_controller = Controller(my_view, my_model)
    my_view.set_controller(my_controller)
    my_view.load_interface()

# Introdurre il seguente codice per visualizzare graficamente il progetto creato
ft.app(target = main)