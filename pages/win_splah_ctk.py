#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Pantalla Inicial(Logo)"""
# 需要实现隐藏边框和标题 Implementar bordes y titulos ocultos

import os
from tkinter import Canvas, Label, Tk, StringVar,CENTER

from PIL import Image, ImageTk

import customtkinter
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue") 

from customtkinter import CTk,CTkImage,CTkButton

import lib.global_variable as glv
from lib.functions import set_window_center


class Splah(CTk):
    """Inicializando Pantalla de bienvenida"""


    def __init__(self):
        CTk.__init__(self)
        self.title("Cargando...")
        self.w = 400
        self.h = 400
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
        
        dark_image_file = os.path.join(
            glv.get_variable("APP_PATH"),
            glv.get_variable("DATA_DIR"),
            "image",
            "dark_splash.jpg",
        )
        canvas = Canvas(self, width=self.w, height=250, bg="white")
        if os.path.exists(image_file):
            my_image = CTkImage(light_image=Image.open(image_file),
                                  dark_image=Image.open(dark_image_file),
                                  size=(180, 180))
            canvas = CTkButton(master=self,width=350, height=350,image=my_image,text="",hover=False)
            #img = Image.open(image_file)  # Abrir Imagen
            #image = ImageTk.PhotoImage(img)  # Abrir con PhotoImage PIL module
            #canvas.create_image(self.w / 2, 250 / 2, image=image)
        else:
            canvas.create_text(
                self.w / 2, 250 / 2, text="CUCEI Inc.(Imagen noesta :c )", font="time 20", tags="string"
            )

        canvas.pack(fill="both")
        
        # Label(self, text="Bienvenidisimo", bg="green", fg="#fff", height=2).pack(
        #    fill="both", side="bottom"
        #)

        text_var = StringVar(value="Bienvenidisimo")
        label = customtkinter.CTkLabel(master=self,
                               textvariable=text_var,
                               width=340,
                               height=80,
                               font=("Consolas",25),
                               fg_color=("#939BA2", "#4A4D50"),
                               corner_radius=25,                               
                               text_color="black"
                               )
        label.place(relx=0.5, rely=0.88, anchor=CENTER)

        # Se establece el tiempo de visualización en x（milliseconds）
        self.after(7500, self.destroy) # 3000 - 4000
        self.mainloop()