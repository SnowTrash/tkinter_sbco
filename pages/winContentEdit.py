#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Content Edit

import tkinter as gui
from lib.functions import set_window_center


class Init(gui.Toplevel):
    """Ventana de edición"""

    def __init__(self, info=None):
        gui.Toplevel.__init__(self)
        self.current_content = info
        self.win_title = "Editar variables de: " + self.current_content["values"][1] + "》"
        self.title(self.win_title)
        set_window_center(self, 400, 500)
        self.resizable(False, False)
        self.init_page()

    def init_page(self):
        """Control de carga"""
        gui.Label(self, text="title").pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Label(self, text="olaolaola")
        msg.pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Message(self, text=self.current_content, width=150)
        msg.pack()
        # gui.Label(self, text="你好你好你好你好").grid()
        # gui.Label(self, text="Parecida a una ventana emergente, con atributos
        #                           de ventana independiente", width=150).grid()
