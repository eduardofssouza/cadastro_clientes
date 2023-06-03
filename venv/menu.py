from tkinter import *
from tkinter import ttk
import sqlite3

file_content = ""
root = Tk()

class Funcs():

    def __init__(self):
        pass

    def limpa_cliente(self):
        pass

    def conecta_bd(self):
        self.conn = sqlite3.connect('clientes.bd')
        self.cursor = self.conn.cursor()
    def desconecta_bd(self):
        self.conn.close()
    def montarTabelas(self):
        self.conecta_bd(); print("Conectando ao banco de dados")
        # Criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
            cod INTEGER PRIMARY KEY,
            nome_cliente CHAR(40) NOT NULL,
            telefone INTEGER(20),
            cidade CHAR(40)
            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgtes_frames()
        self.lista_frame2()
        self.montarTabelas()
        root.mainloop()
        
    def tela(self):
        self.root.title("Gerador de Escalas")
        self.root.configure(background= '#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg= "#B0C4DE", 
                             highlightbackground= "white", highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg= "#B0C4DE", 
                             highlightbackground= "white", highlightthickness=3)
        self.frame_2.place(relx=0.02 , rely=0.5, relwidth=0.96, relheight=0.46)

    def widgtes_frames(self):
        ##Criar botão limpar
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#D3D3D3', fg='Black', 
                                font = ('verdana', 8, 'bold'))
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        ##Criar botão buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#D3D3D3', fg='Black', 
                                font = ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        ##Criar botão executar
        self.bt_novo = Button(self.frame_1, text='Novo', bd=2, bg='#D3D3D3', fg='Black', 
                                font = ('verdana', 8, 'bold'))
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

       ##Criar botão re-otimizar
        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#D3D3D3', fg='Black', 
                                font = ('verdana', 8, 'bold'))
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
 
        ##Criar botão limpar
        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=2, bg='#D3D3D3', fg='Black', 
                                font = ('verdana', 8, 'bold'))
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ##Criação da label e entrada do codigo
        self.lb_codigo = Label(self.frame_1, text = "Código", bg= "#B0C4DE")
        self.lb_codigo.place(relx=0.05, rely=0.04)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        ##Criação da label nome cliente
        self.lb_nome = Label(self.frame_1, text ="Nome", bg= "#B0C4DE")
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        ##Criação da label telefone
        self.lb_telefone = Label(self.frame_1, text ="Telefone", bg= "#B0C4DE")
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        ##Criação da label cidade
        self.lb_cidade = Label(self.frame_1, text ="Cidade", bg= "#B0C4DE")
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

    def lista_frame2(self):
        self.listacl1 = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        self.listacl1.heading('#0', text="")
        self.listacl1.heading('#1', text="Codigo")
        self.listacl1.heading('#2', text="Nome")
        self.listacl1.heading('#3', text="Telefone")
        self.listacl1.heading('#4', text="Cidade")
        
        self.listacl1.column('#0', width=1)
        self.listacl1.column('#1', width=50)
        self.listacl1.column('#2', width=200)
        self.listacl1.column('#3', width=125)
        self.listacl1.column('#4', width=125)

        self.listacl1.place(relx=0.01 , rely=0.01, relwidth=0.95, relheight=0.95)

        self.scroolista = Scrollbar(self.frame_2, orient='vertical')
        self.listacl1.configure(yscroll=self.scroolista.set)
        self.scroolista.place(relx=0.96 ,rely=0.01, relwidth=0.035, relheight=0.95)

Application()