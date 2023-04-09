#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Pantalla Inicial(Logo)"""
# 需要实现隐藏边框和标题 ¿¿Implementar bordes y titulos ocultos??

import os
from tkinter import Canvas, Label, Tk

# from PIL import Image, ImageTk

import lib.global_variable as glv
from lib.functions import set_window_center


class Splah(Tk):
    """Inicializando Pantalla de bienvenida"""

    def __init__(self):
        Tk.__init__(self)
        self.title("Cargando...")
        self.w = 300
        self.h = 300
        set_window_center(self, self.w, self.h)
        self.resizable(False, False)
        self.splash()

    def splash(self):
        """Pantalla de Inicio"""
        image_file = os.path.join(
            glv.get_variable("APP_PATH"),
            glv.get_variable("DATA_DIR"),
            "image",
            "splash.jpg",
        )
        canvas = Canvas(self, width=self.w, height=250, bg="white")
        # if os.path.exists(image_file):
        #     img = Image.open(image_file)  # Abrir Imagen
        #     image = ImageTk.PhotoImage(img)  # Abrir con PhotoImage PIL module
        #     canvas.create_image(self.w / 2, 250 / 2, image=image)
        # else:
        canvas.create_text(
            self.w / 2, 250 / 2, text="CUCEI Inc.", font="time 20", tags="string"
        )

        canvas.pack(fill="both")
        Label(self, text="Bienvenidisimo", bg="green", fg="#fff", height=2).pack(
            fill="both", side="bottom"
        )

        # Se establece el tiempo de visualización en x（milliseconds）
        self.after(4713, self.destroy)
        self.mainloop()
