#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""程序入口文件 Archivo Principal del programa"""

import os
from tkinter import Tk

from customtkinter import CTk

import lib.global_variable as glv
from pages import win_login_ctk, win_splah_ctk

# Load global variable management module 
glv.init_global_variable()
glv.set_variable("APP_NAME", "Application")
glv.set_variable("APP_PATH", os.path.dirname(__file__))  # 当前目录 Directorio actual
glv.set_variable("DATA_DIR", "data")

class App(CTk):
    """Application Class"""
    def __init__(self):

        win_splah_ctk.Splah() # Arreglar transparencias y estilos
        CTk.__init__(self)

        # 登录窗口 Login Window
        win_login_ctk.Login(self) # Utilizar CustomTkinter
        self.mainloop()

if __name__ == "__main__":
    App()
