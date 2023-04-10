#!/usr/bin/env python3
# -*- coding:utf-8-*-

#Modificando UI con customtkinter

import tkinter.messagebox
from tkinter import CENTER,StringVar

import customtkinter
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")

from customtkinter import CTk,CTkButton,CTkLabel

from lib.functions import set_window_center
from lib.sqlite_helper import DBHelper

#importamos la app con el prefijo de CustomTkinter
from main_ctk import App


class InitWindow(CTk):
    """Inicializando Ventana"""

    def __init__(self):
        CTk.__init__(self)
        self.title("Inicializando Datos")
        self.w = 400
        self.h = 400
        set_window_center(self, 200, 180)
        self.resizable(False, False)
        self.win_success = None # Bandera de Inicialización exitosa
        self.init_page()

    def init_page(self):
        """Control de carga"""
        btn_1 = CTkButton(self, text="Crear base de datos", command=self.do_init_db)
        btn_1.pack(expand="yes", padx=10, pady=10, ipadx=5, ipady=5)

    def do_init_db(self):
        """Inicialización"""
        db_helper = DBHelper()
        db_helper.reset_database()
        db_helper.create_database()
        try:
            tmp = db_helper.insert_user("admin", "admin")  # Usuario predeterminado
            tmp2 = db_helper.insert_content_by_username(   # Insertamos una filona
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
        """Fallo , intentar de nuevo?"""
        res = tkinter.messagebox.askretrycancel('Solicitud', 'Falló la inicialización, ¿intentarlo de nuevo?', parent=self)
        if res is True:
            self.do_init_db()
        elif res is False:
            self.destroy()

    def do_success(self):
        """Inicialización Exitosa chinyi"""
        text_var = StringVar(value="Base de datos creada con éxito")
        self.win_success = CTk()
        self.win_success.title("Inicialización Exitosa")
        self.win_success.w = 400
        self.win_success.h = 400
        set_window_center(self.win_success, 250, 150)
        self.win_success.resizable(False, False)
        msg = CTkLabel(master=self.win_success,
                               textvariable=text_var,
                               width=120,
                               height=25,
                               fg_color=("white", "gray75"),
                               corner_radius=8)
        msg.place(relx=0.5, rely=0.5, anchor=CENTER)

        #msg.pack(expand="yes", fill="both")


        button1 = customtkinter.CTkButton(master=self.win_success,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="OK",
                                 command=self.quit)
        button1.place(relx=0.24, rely=0.75, anchor=CENTER)

       # btn = Button(self.win_success, text="OK", command=self.quit)
       # btn.pack(side="right", padx=10, pady=10, ipadx=5, ipady=5)


        button2 = customtkinter.CTkButton(master=self.win_success,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Iniciar el programa",
                                 command=self.open_app)
        button2.place(relx=0.75, rely=0.75, anchor=CENTER)

        #btn_open_app = Button(self.win_success, text="Iniciar el programa", command=self.open_app)
        #btn_open_app.pack(side="right", padx=10, pady=10, ipadx=5, ipady=5)

    def open_app(self):
        """Abrir la app - main.py"""
        self.quit()
        self.win_success.destroy()
        self.win_success.quit()

        App()

if __name__ == "__main__":
    APP_INIT = InitWindow()
    APP_INIT.mainloop()
