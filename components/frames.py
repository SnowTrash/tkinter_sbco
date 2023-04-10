# Los comentarios al final de los renglones con strings "xxxx"
# que definen textos del front-end, son strings originales en chino 
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import (Button, Label, Frame, Entry, LabelFrame, StringVar, messagebox,
                     scrolledtext, ttk)

import lib.dbcontent as dbcontent
from lib import global_variable
from lib.functions import treeview_sort_column
from pages import win_user_edit, win_user_info, winContentEdit, winContentInfo


class HomeFrame(Frame):  # Heredado de Frame
    """UI principal"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent  # Definimos el root de la variable interna
        self.init_page()

    def init_page(self):
        """Cargar elementos al Frame"""
        Label(self, text="Usuario:").pack()

        Label(self, text="Bienvenido --> " + str(global_variable.get_variable("CURRENT_USER_NAME"))+ "<--").pack()
        Button(self, text="Ver").pack()


class ContentAdd(Frame):
    """Añadir Artículo"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent  # Definimos la pestaña actual como raíz
        self.content_title = StringVar()
        self.content_textarea = None
        self.content_tag = StringVar()
        self.init_page()

    def init_page(self):
        """Cargando Página"""
        Label(self).grid(row=0, stick="w", pady=10)

        lb1 = Label(self, text="Título: ")
        lb1.grid(row=1, stick="w", pady=10)

        et1 = Entry(self, textvariable=self.content_title)
        et1.grid(row=1, column=1, stick="we")

        lb2 = Label(self, text="Contenido: ")
        lb2.grid(row=2, stick="nw", pady=10)

        et2 = scrolledtext.ScrolledText(
            self,
            height=10,
            font=("Courier New", 13),
            fg="#333",
            borderwidth=1,
            highlightcolor="#ddd",
        )
        et2.grid(row=2, column=1, ipadx=10, stick="nswe")
        self.content_textarea = et2

        lb3 = Label(self, text="etiqueta: ")
        lb3.grid(row=3, stick="w", pady=10)

        et3 = Entry(self, textvariable=self.content_tag)
        et3.grid(row=3, column=1, columnspan=2, stick="we")

        bt1 = Button(self, text="Añadir", command=self.do_add)
        bt1.grid(row=6, column=1, stick="e", pady=10)

    def do_add(self):
        """Añadir Artículo"""
        title = self.content_title.get()
        content = self.content_textarea.get(0.0, "end")
        tag = self.content_tag.get()
        username = str(global_variable.get_variable("CURRENT_USER_NAME"))
        res = dbcontent.content_add(username, title, content, tag)
        if res is True:
            self.content_title.set("")
            self.content_tag.set("")
            self.content_textarea.delete(1.0, "end")  # 清空
            self.content_textarea.update()
            messagebox.showinfo(title="Éxito", message="Agregado a DB correctamente")
        else:
            messagebox.showinfo(title="Error", message="Error en el Update-add")


class ContentList(Frame):
    """Lista de Artículos"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.list = []
        self.selected_item = None
        self.selected_name = StringVar()
        self.win_content_info = None
        self.win_content_edit = None
        self.init_page()

    def init_page(self):
        """Creando página"""

        username = str(global_variable.get_variable("CURRENT_USER_NAME"))
        self.list = dbcontent.content_list_by_username(username)

        head_frame = LabelFrame(self, text="Listado de artículos")
        head_frame.grid(row=0, column=0, columnspan=2, sticky="nswe")
        Label(head_frame, textvariable=self.selected_name).pack()

        btn_info = Button(head_frame, text="Detalles", command=self.info)
        btn_info.pack(side="left")
        btn_edit = Button(head_frame, text="Editar", command=self.edit)
        btn_edit.pack(side="left")
        btn_delete = Button(head_frame, text="Borrar", command=self.delete)
        btn_delete.pack(side="left")

        # 表格 ¿¿Hoja Dataframe??
        self.tree_view = ttk.Treeview(self, show="headings")

        self.tree_view["columns"] = ("id", "title", "content", "tag")
        # 列设置 Configuración de columna
        self.tree_view.column("id", width=100)
        # self.tree_view.column("title", width=100)
        # self.tree_view.column("content", width=100)
        # self.tree_view.column("tag", width=100)
        # 显示表头 Mostramos el encabezado
        self.tree_view.heading("id", text="ID")
        self.tree_view.heading("title", text="标题")
        self.tree_view.heading("content", text="内容")
        self.tree_view.heading("tag", text="标签")

        # 插入数据 Insertamos los datos
        num = 1
        for item in self.list:
            self.tree_view.insert(
                "",
                num,
                text="",
                values=(item["id"], item["title"], item["content"], item["tag"]),
            )
        # 选中行 Selecionamos la fila
        self.tree_view.bind("<<TreeviewSelect>>", self.select)

        # 排序 Seleccionamos la columna
        for col in self.tree_view["columns"]:  # 给所有标题加 Recorremos y agregamos los encabezados
            self.tree_view.heading(
                col,
                text=col,
                command=lambda _col=col: treeview_sort_column(
                    self.tree_view, _col, False
                ),
            )

        vbar = ttk.Scrollbar(self, orient="vertical", command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vbar.set)
        self.tree_view.grid(row=1, column=0, sticky="nsew")
        vbar.grid(row=1, column=1, sticky="ns")

    def select(self, event):
        """选中 Seleccionar"""
        # event.widget获取Treeview对象，调用selection获取选择所有选中的
        # event.widget contiene el Treeview para poder llamar a 
        #                                   los elementos seleccionados
        slct = event.widget.selection()[0]
        self.selected_item = self.tree_view.item(slct)
        self.selected_name.set(self.selected_item["values"][1])
        # print("you clicked on ", self.selected_item)
        # print(self.selected_name)

    def info(self):
        """详情 Detalles"""
        print("Detalles", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("Preguntar", "Seleccione primero") # "提示", "请先选择"
        else:
            if self.win_content_info is not None and hasattr(self.win_content_info.destroy, "__call__"):
                # if self.win_content_info and self.win_content_info.destroy:
                self.win_content_info.destroy()
            self.win_content_info = winContentInfo.Init(self.selected_item)
            # self.win_content_info = winAbout.Init()

    def edit(self):
        """编辑 Editar"""
        print("editar", self.selected_item) # 编辑
        if self.selected_item is None:
            messagebox.showinfo("Pregunta", "Seleccione un objeto1 primero") # 提示 , 请先选择
        else:
            if self.win_content_edit and self.win_content_edit.destroy:
                self.win_content_edit.destroy()
            self.win_content_edit = winContentEdit.Init(self.selected_item)

    def delete(self):
        """删除 Borrar"""
        print(self.selected_item)
        messagebox.showinfo("Seguro quiere ELIMINAR \n ？？？ \n ---->", self.selected_item)  # 删除？ 弹出消息提示框


class CountFrame(Frame):
    """文章统计 Control de Ventanas"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.init_page()

    def init_page(self):
        """加载控件 Cargando """
        Label(self, text="Interfaz de estadísticas").pack() # 统计界面


class AboutFrame(Frame):
    """关于界面 Acerca de:"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.init_page()

    def init_page(self):
        """加载控件 Cargando pantalla"""
        # Label(self, text="关于界面").grid()
        Label(self, text="你好你好holahola").grid()
        Label(self, text="类似于弹出窗口，具有独立的窗口属性。", width=150).grid()


class UserListFrame(Frame):
    """用户列表界面 Interfaz de los usuarios"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.list = []
        self.selected_item = None
        self.selected_name = StringVar()
        self.win_user_info = None
        self.win_user_edit = None
        self.init_page()

    def init_page(self):
        """加载控件 Cargando ventana"""

        self.list = dbcontent.user_list()

        head_frame = LabelFrame(self, text="Modificar Usuario") # 用户操作
        head_frame.grid(row=0, column=0, columnspan=2, sticky="nswe")
        Label(head_frame, textvariable=self.selected_name).pack()

        btn_info = Button(head_frame, text="Detalles", command=self.info) # 详情
        btn_info.pack(side="left")
        btn_edit = Button(head_frame, text="Editar", command=self.edit) # 编辑
        btn_edit.pack(side="left")
        btn_reset = Button(head_frame, text="Resetear contraseña", command=self.reset) # 重置密码
        btn_reset.pack(side="left")
        btn_delete = Button(head_frame, text="Borrar/Eliminar", command=self.delete)
        btn_delete.pack(side="left")

        # 表格 Dataframe Hoja/tabla
        self.tree_view = ttk.Treeview(self, show="headings")

        self.tree_view["columns"] = ("id", "name", "password", "op")
        # 列设置 Mostrar los encabezados
        # self.tree_view.column("id", width=100) # 表示列,不显示 Indica la columna
        # self.tree_view.column("name", width=100)
        # self.tree_view.column("password", width=100)
        # self.tree_view.column("op", width=100)
        # 显示表头
        self.tree_view.heading("id", text="ID")
        self.tree_view.heading("name", text="Nombre") # 姓名
        self.tree_view.heading("password", text="Contraseña") # 姓名
        self.tree_view.heading("op", text="Operación") # 操作

        # 插入数据 Insertar datos
        num = 1
        for item in self.list:
            self.tree_view.insert(
                "",
                num,
                text="",
                values=(item["id"], item["name"], item["password"], "detalles"),
            )
        # 选中行 Seleccionamos la fila
        self.tree_view.bind("<<TreeviewSelect>>", self.select)

        # 排序 Clasificar
        for col in self.tree_view["columns"]:  # 给所有标题加 Se agregan/iteran los encabezados
            self.tree_view.heading(
                col,
                text=col,
                command=lambda _col=col: treeview_sort_column(
                    self.tree_view, _col, False
                ),
            )

        vbar = ttk.Scrollbar(self, orient="vertical", command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vbar.set)
        self.tree_view.grid(row=1, column=0, sticky="nsew")
        vbar.grid(row=1, column=1, sticky="ns")
        Label(self, text="Barra de operaciones inferior").grid(sticky="swe")

    def select(self, event):
        """选中 Seleccionar"""
        # event.widget获取Treeview对象，调用selection获取选择所有选中的
        slct = event.widget.selection()[0]
        self.selected_item = self.tree_view.item(slct)
        self.selected_name.set(self.selected_item["values"][1])

    def info(self):
        """详情 Detalles"""
        print("Detalles", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("Pregunta", "Seleccione un item primero")  # "提示", "请先选择"
        else:
            if self.win_user_info is not None and (
                hasattr(self.win_user_info.destroy, "__call__")
            ):
                self.win_user_info.destroy()
            self.win_user_info = win_user_info.Init(self.selected_item)

    def edit(self):
        """用户编辑 Editar usuarios"""
        print("Editar:", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("Pregunta", "Seleccione un item primero")  # "提示", "请先选择"
        else:
            if self.win_user_edit is not None and hasattr(
                self.win_user_edit.destroy, "__call__"
            ):
                self.win_user_edit.destroy()
            self.win_user_edit = win_user_edit.Init(self.selected_item)

    def delete(self):
        """用户删除 Eliminar usuario"""
        print(self.selected_item)
        messagebox.showinfo("Borrar al usuario?？ ", self.selected_item)  # 删除用户？  弹出消息提示框

    def reset(self):
        """用户删除 Eliminar usuario"""
        print("Usuario Eliminado con Éxito ") # 用户删除


class UserAddFrame(Frame):
    """用户添加 Agregar usuario"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.username = StringVar()
        self.password = StringVar()
        self.init_page()

    def init_page(self):
        """加载控件 Cargando componentes"""
        Label(self).grid(row=0, stick="w")

        Label(self, text="Usuario: ").grid(row=1, stick="w", pady=10) # 账户
        username = Entry(self, textvariable=self.username)
        username.grid(row=1, column=1, stick="e")

        Label(self, text="Contraseña: ").grid(row=2, stick="w", pady=10) # 密码
        password = Entry(self, textvariable=self.password, show="*")
        password.grid(row=2, column=1, stick="e")

        button_login = Button(self, text="Añadir", command=self.do_add) # 添加
        button_login.grid(row=3, column=1, stick="w", pady=10)

    def do_add(self):
        """添加帐号 Añadir Usuario al DB"""
        # print(event)
        username = self.username.get()
        password = self.password.get()
        res = dbcontent.user_add(username, password)
        if res is True:
            self.username.set("")
            self.password.set("")
            messagebox.showinfo(title="Exito", message="Usuario Añadido con éxito") # 成功 添加成功
        else:
            messagebox.showinfo(title="Error", message="Ese usuario ya existe") # 错误 账号已存在
