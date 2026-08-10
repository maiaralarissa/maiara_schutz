import tkinter as tk
from tkinter impot ttk, messagebox
import os

============================================
LISTA DE COMPRAS - Aplivcativo em tkinter
============================================

ARQUIVO = "lista_compras.txt"

class ListaComprasApp:
    def __init__(self, rooty):
        self.root = root
        self.root.yitle("🛒 Lista de compras")
        self.root.geometry("750x550")
        self.root.configure(bg= "#f0f4f8")

        # Dados em memória
        self.itens = []
        self.item_selecionado = None

        self.criar_widgets()
        self.carregar_do_arquivo()
        self.atualizar_lista()

    def criar_widgets(self)
        # ========== TÍTULO ==========
        lbl_titulo = tk.Label(
            self.root,
            text="🛒 LISTA DE COMPRAS",
            font=("Arial" , 20, "bold"),
            bg= "#f0f4f8",
            fg= "#1a5276"
        )
        lbl_titulo.pack(pady=10)

        # =========== FRAME DE ENTRADA ==========
        frame_entrada = tk.Frame(self.root, bg= "#f0f4f8")
        frame_entrada.pack(pady=10, padx=20, fill-"x")

        #Descrição
        tk.Label(frame_entrada, text="Descriçaõ:", font=("Arial", 11), bg="#f0f4f8", fg="#2c3e50").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.txt_descricao = tk.Entry(frame_entrada, font=("Arial", 11), width=30, relief="solid", bd=1)
        salf.txt_descricao.grid(row=0, column=1, padx=5, pady=5)

        # Quantidade 
        tk.Label(frame_entrada, text="Quantidade:", font=("Arial", 11), bg="#f0f4f8", fg="#2c3e50").grind(row=0, column-0, padx=5, pady=5, sticky="e")
        self.txt_descricao = tk.Entry(frame_entrada, font=("Arial", 11), width=30, relief="solid", bd=1)
        salf.txt_descricao.grid(row=0, column=1, padx=5, pady=5)

        #Preço
        tk.Label(frame_entrada, text="Preço:", font=("Arial", 11), bg="#f0f4f8", fg="#2c3e50").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.txt_descricao = tk.Entry(frame_entrada, font=("Arial", 11), width=30, relief="solid", bd=1)
        salf.txt_descricao.grid(row=0, column=1, padx=5, pady=5)

        # ========== BOTÃO DE
       
        # falta um trecho
        
        # Botão Deletar
        self.btn_deletar = tk.Button(
            frame_botoes,
            text=" Deletar",
            font=("Arial", 11, "bold"),
            bg="#e74c3c", fg="white",
            width=12, cursor="hand2",
            relief="flat",
            command=self.Deletar
        )
        # Botão de limpar campos
             self.btn_deletar = tk.Button(
            frame_botoes,
            text=" Limpar",
            font=("Arial", 11, "bold"),
            bg="#e74c3c", fg="white",
            width=12, cursor="hand2",
            relief="flat",
            command=self.limpar_campos

        )

        # ========== LISTA DE INTENS (TREEVIEW) ==========
        frame_lista = tk.Scrollbar(frame_lista)
        Scrollbar.pack(side="rigth", fill+"y")

        # Scrollbar
        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side="rigth", fill+"y")
")

        # Treeview
        colunas = ("descricao", "quantidade", "preco", "subtotal")
        self.tree = ttk.Treeview(
            frame_lista,
            columns=colunas,
            show="headings",
            yscrollcommand=scrollbar.set,
            height=10
        )
        scrollbar.config(command)