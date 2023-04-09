#!/usr/bin/env python3
# -*- coding:utf-8-*-

import tkinter.messagebox
from tkinter import Button, Label, Tk

from lib.functions import set_window_center
from lib.sqlite_helper import DBHelper

#importamos la app
from main import App


class InitWindow(Tk):
    """Inicializando Ventana"""

    def __init__(self):
        Tk.__init__(self)
        self.title("Inicializando Datos")
        set_window_center(self, 300, 180)
        self.resizable(False, False)
        self.win_success = None # Aviso de Inicialización exitosa
        self.init_page()

    def init_page(self):
        """Control de carga"""
        btn_1 = Button(self, text="Crear base de datos", command=self.do_init_db)
        btn_1.pack(expand="yes", padx=10, pady=10, ipadx=5, ipady=5)

    def do_init_db(self):
        """Inicialización"""
        db_helper = DBHelper()
        db_helper.reset_database()
        db_helper.create_database()
        try:
            tmp = db_helper.insert_user("admin", "admin")  # Usuario predeterminado
            tmp2 = db_helper.insert_content_by_username(
                "admin",
                "Hello World !",
                "Codigo fuente：https://github.com/SnowTrash/tkinter_sbco",
                "github",
            )
            tmp3 = db_helper.get_content_by_username("admin")
            print("Agregar usuario-admin:", tmp)
            print("Agregar contenido:", tmp2)
            print("consulta:", tmp3)
            self.do_success()
            self.destroy()
        except KeyError:
            print(KeyError)
            self.do_failed()

    def do_failed(self):
        """Rever"""
        res = tkinter.messagebox.askretrycancel('Solicitud', 'Falló la inicialización, ¿intentarlo de nuevo?', parent=self)
        if res is True:
            self.do_init_db()
        elif res is False:
            self.destroy()

    def do_success(self):
        """Inicialización Exitosa chinyi"""
        self.win_success = Tk()
        self.win_success.title("Base de datos creada con éxito")
        set_window_center(self.win_success, 250, 150)
        self.win_success.resizable(False, False)
        msg = Label(self.win_success, text="Inicialización exitosa")
        msg.pack(expand="yes", fill="both")

        btn = Button(self.win_success, text="OK", command=self.quit)
        btn.pack(side="right", padx=10, pady=10, ipadx=5, ipady=5)
        btn_open_app = Button(self.win_success, text="Iniciar el programa", command=self.open_app)
        btn_open_app.pack(side="right", padx=10, pady=10, ipadx=5, ipady=5)

    def open_app(self):
        """Abrir la app - main.py"""
        self.quit()
        self.win_success.destroy()
        self.win_success.quit()

        App()


if __name__ == "__main__":
    APP_INIT = InitWindow()
    APP_INIT.mainloop()
