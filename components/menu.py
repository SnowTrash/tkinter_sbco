# Los comentarios al final de los renglones con strings "xxxx"
# que definen textos del front-end, son strings originales en chino 
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import Menu, messagebox

class MainMenu:
    """主界面菜单 - Menú principal"""

    def __init__(self, master):
        """初始化菜单 - Inicializamos el menú"""
        self.master = master # 上级
        self.root = master.root # 主窗口
        self.init_menu()

    def init_menu(self):
        """加载菜单 Declaramos la barra de """

        # 创建菜单栏 - Crea la barra de menú
        self.menubar = Menu(self.root)

        # 将菜单栏添加到窗口 - Agrega a la ventana 
        self.root.config(menu=self.menubar)

        # 文件下拉菜单 - Menú de archivo
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Nuevo", command=self.file_new) # 新建",
        filemenu.add_command(label="Abrir", command=self.file_open) # 打开",
        filemenu.add_command(label="Guradar", command=self.file_save) # 保存",
        filemenu.add_command(label="Guardar como...", command=self.file_save) # ="另存为
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.root.quit) # 退出

        # 用户下拉菜单 - Menú de usuario
        usermenu = Menu(self.menubar, tearoff=0)
        usermenu.add_command(label="Lista de usuarios", command=self.master.open_user_list) # 用户列表
        usermenu.add_command(label="Agregar usuario", command=self.master.open_user_add) # 用户添加
        usermenu.add_command(label="Detalles del usuario", command=self.master.open_user_info) # 用户详情窗口

        # 文章下拉菜单 Menú de articulos
        articlemenu = Menu(self.menubar, tearoff=0)
        articlemenu.add_command(label="Consultar articulo", command=self.master.open_content_list) # 文章查询
        articlemenu.add_command(label="Agregar articulo", command=self.master.open_content_add) # 文章添加
        articlemenu.add_command(label="Detalles/estadísticas de artículo", command=self.master.open_content_count) # 文章统计

        # 数据下拉菜单 Menú de DB
        datamenu = Menu(self.menubar, tearoff=0)
        datamenu.add_command(label="Descargar", command=self.master.open_download) # 下载
        datamenu.add_command(label="Cargar", command=self.master.open_upload)   # 上传
        datamenu.add_command(label="Sincronizar", command=self.master.open_synchronize) # 同步
        datamenu.add_command(label="Abrir Respaldo", command=self.master.open_backup) # 备份

        # 窗口下拉菜单 Ventana del Menú
        window_menu = Menu(self.menubar)
        window_menu.add_command(label="Maximizar") # 最大化
        window_menu.add_command(label="Minimizar") # 最小化
        window_menu.add_separator()
        window_menu.add_command(label="Traer al Frente", command=self.master.window_to_top) # 窗口置顶
        window_menu.add_command(label="Enviar atrás", command=self.master.window_not_top) # 取消置顶
        window_menu.add_separator()
        window_menu.add_command(label="Interfaz Principal", command=self.master.open_home) # 主界面
        window_menu.add_command(label="Ir a: Usuario") # 切换到: 用户
        window_menu.add_command(label="Ir a: Lista de articulos") # 切换到: 文章列表

        # 帮助下拉菜单 Menú de ayuda
        helpmenu = Menu(self.menubar)
        helpmenu.add_command(label="Bienvenido", command=self.help_about) # 欢迎使用
        helpmenu.add_command(label="Documentación", command=self.help_about) # 文档
        helpmenu.add_command(label="Derechos de Autor", command=self.help_about) # 版权声明
        helpmenu.add_command(label="Privacidad", command=self.help_about) # 隐私声明
        helpmenu.add_separator()
        helpmenu.add_command(label="Contactanos", command=self.master.open_ontact) # 联系我们
        helpmenu.add_command(label="Acerca de", command=self.master.open_about) # 关于

        # 将下拉菜单加到菜单栏 Agregar submenús al principal
        self.menubar.add_cascade(label="Archivo", menu=filemenu) # "文件"
        self.menubar.add_cascade(label="Usuario", menu=usermenu) # "用户"
        self.menubar.add_cascade(label="Articulo", menu=articlemenu) # "文章"
        self.menubar.add_cascade(label="Datos", menu=datamenu) # "数据"
        self.menubar.add_cascade(label="Ventana", menu=window_menu) # "窗口"
        self.menubar.add_cascade(label="Ayuda", menu=helpmenu) # "帮助"

    def file_open(self):
        messagebox.showinfo("Abrir", "Abrir Archivo")  # 消息提示框 Mensaje de Aviso (Abrir - Archivo Abrir)

    def file_new(self):
        messagebox.showinfo("Nuevo", "Archivo Nuevo！")  # 消息提示框 Nuevo - Archivo Nuevo!

    def file_save(self):
        messagebox.showinfo("Guardar", "Guardar Archivo！")  # 消息提示框 Guardar - Guardar archivo!

    def edit_cut(self):
        messagebox.showinfo("Copiar", "Editar-Cortar！")  # 消息提示框 Copiar Editar-Cortar

    def edit_copy(self):
        messagebox.showinfo("Copiar", "Editar-Copiar！")  # 消息提示框 Copiar Editar-Copiar

    def edit_paste(self):
        messagebox.showinfo("Pegar", "¡Editar-Pegar！")  # 消息提示框 Pegar Editar-Pegar!

    def help_about(self):
        """关于 Sobre nosotros"""
        messagebox.showinfo(
            "About", "作者: doudoudzj \n version 1.0 \n doudoudzj@sina.com \n\n 业余翻译: snowtrash \n version 1.0.1 \n juan.vargas2962@alumnos.udg.mx"
        )
