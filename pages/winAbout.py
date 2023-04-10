#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""About - Sobre el proyecto"""

from tkinter import Tk, Label, Message, Toplevel

# import lib.global_variable as glv
# from lib.functions import set_window_center
# Estos imports se pueden utilizar cuando se manipulen las variables
# que obtiene el modulo lib/global_variables


class Init(Tk):
    """About"""

    def __init__(self):
        Tk.__init__(self)
        self.title("")
        # set_window_center(self, 400, 400)
        self.app_name = "Python Tkinter Application" # glv.get_variable("APP_NAME")
        self.app_version = "0.1.1"
        self.app_desc = "Aplicacion para seguimiento de pacientes"
        self.app_url = "https://SnowTrash.com"
        self.app_ = "Copyright © 2023 XXXX. All rights reserved."
        # self.resizable(False, False)
        self.init_page()

    def init_page(self):
        """Creando la pantalla"""
        Label(self, text="LOGO").pack(fill="both")
        Label(self, text=self.app_name).pack()
        Label(self, text=self.app_version).pack()
        Label(self, text=self.app_url).pack()
        Label(self, text=self.app_).pack()
        Message(self, text=self.app_desc).pack()
        # Label(self, text="你好你好你好holahola").grid()
        # Label(self, text="ventana emergenteatriutos indepen", width=150).grid()

if __name__ == "__main__":
    APP_ABOUT = Init()
    APP_ABOUT.mainloop()