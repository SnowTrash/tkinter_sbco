#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import Toplevel, Label, Message
from components import frames, menu
from lib.functions import set_window_center
from pages import winAbout


class MainPage():
    """主界面 Interfaz Principal"""

    def __init__(self, master=None):
        self.root = master # 主窗口 ventana principal
        set_window_center(self.root, 800, 600)
        menu.MainMenu(self) # 使用self可以传递主窗口和主窗口操作函数 
                            # utiliza self para pasar la ventana
                            # y las funciones que necesita
        # 初始化Frames - Definimos las ventanas
        self.current_frame = None
        self.page_frame = {
            "home": frames.HomeFrame,
            "content_add": frames.ContentAdd,
            "content_list": frames.ContentList,
            "count": frames.CountFrame,
            "contact": frames.AboutFrame,
            "user_list": frames.UserListFrame,
            "user_add": frames.UserAddFrame
        }
        self.open_home()
        self.win_about = None

    def open_page(self, frame_name, title):
        """打开/更换主界面的通用函数 Función para stackear las ventanas y navegar"""
        self.root.title(title)
        # 先销毁之前frame - Destruye la pantalla actual en caso de ser distinta a Nulo
        if self.current_frame is not None and (hasattr(self.current_frame.destroy, '__call__')):
            self.current_frame.destroy()

        self.current_frame = self.page_frame[frame_name](self.root)
        self.current_frame.pack()

    def open_home(self):
        """应用主界面 Home"""
        self.open_page("home", "Pagina Principal")

    def open_content_add(self):
        """文章添加 Agregar Articulo"""
        self.open_page("content_add", "Agregar Artículo")

    def open_content_list(self):
        """文章列表 Consultar Articulos"""
        self.open_page("content_list", "Listado de Articulos")

    def open_content_count(self):
        """文章统计 Detalles/estadisticas del artículo"""
        self.open_page("count", "Detalles / Estadísticas")

    def open_ontact(self):
        """联系我们"""
        self.open_page("contact", "Contactanos")

    def open_user_info(self):
        """用户详情"""
        page = Toplevel()
        page.title("Detalles de usuario")
        page.resizable(False, False)
        set_window_center(page, 200, 150)

        # Label(page).grid(row=0, stick="w", pady=2)

        Label(page, text="Nombre: ").grid(row=1, stick="w", pady=2) # 姓名
        Label(page, text="Admin").grid(row=1, column=1, stick="e") # 管理员

        Label(page, text="Usuario: ").grid(row=2, stick="w", pady=2) # 账户
        Label(page, text="admin").grid(row=2, column=1, stick="e")

        Label(page, text="Constraseña: ").grid(row=3, stick="w", pady=2) # 密码
        Label(page, text="admin").grid(row=3, column=1, stick="e")

    def open_user_list(self):
        """用户列表 Detalles de usuario"""
        self.open_page("user_list", "Lista de Usuarios")
        # self.page_frame['user_list'].init_data()

    def open_user_add(self):
        """用户添加"""
        self.open_page("user_add", "Agregar Usuario")

    def open_download(self):
        """下载窗口 Ventana de descargas"""
        root = Toplevel()
        root.title("下载管理")
        set_window_center(root, 400, 400)
        msg = Label(root, text="你好ñola")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()

    def open_upload(self):
        """上传管理 Gestor de uploads"""
        root = Toplevel()
        root.title("上传管理")
        set_window_center(root, 400, 400)
        msg = Label(root, text="你好你好你好你好")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()

    def open_synchronize(self):
        """同步管理 Gestor de Sincronización"""
        root = Toplevel()
        root.title("同步管理")
        set_window_center(root, 400, 400)
        msg = Label(root, text="你好你好你好你好")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()

    def open_backup(self):
        """备份管理 Gestión de Backup, respaldos"""
        root = Toplevel()
        root.title("Administrar Respaldos")
        set_window_center(root, 400, 400)
        msg = Label(root, text="你好你 Mundo ola")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()

    def open_about(self):
        """关于窗口 Acerca de:"""
        if self.win_about and self.win_about.destroy:
            self.win_about.destroy()
        self.win_about = winAbout.Init()

    def window_to_top(self):
        """窗口置顶 Ventana arriba"""
        self.root.attributes('-topmost', True)

    def window_not_top(self):
        """窗口置顶 Ventana abajo"""
        self.root.attributes('-topmost', False)
