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

         # ================ FRAME DE BOTOẼS ================
    frame botoes = tk.Frame(self.root, bg="#f0f4f8")
    frame botoes.pack(pady=10)

    #Botão inserir
    self.btn_inserir = tk.Button(
      frame_botoes,
      text="🏥inserir",
      font=("Arial", 11, "bold")
      bg="#f0f4f8", fg("white")
      width=12, cursor="hand2",
      relief="flat",
      command=self.inserir
    )
    self.btn_inserir.pack(side="left", padx=5)
   
    # Botão Editar
    self.btn_editar = tk.Button(
      frame_botoes,
      text="- Editar",
      font=("Arial", 11, "bold"),
      bg="#f39c12", fg="White",
      width=12, cursor="hand2"
      relief="flat",
      command=self.editar
    )
    self.btn_editar.pack(side="left", padx=5)
   
    # Botão Deletar
    self.btn_deletar = tk.Button(
      frame_botoes,
      text="🗑️ Deletar",
      font=("Arial", 11, "bold"),
      bg="#e74c3c", fg="White",
      width=12, cursor="hand2",
      relief="flat",
      command=self.Deletar
    )
    self.btn_deletar.pack(side="left", padx=5)

    # Botão limpar campos
    self.btn_inserir = tk.Button(
      frame_botoes,
      text="limpar",
      font=("Arial", 11, "bold")
      bg="#f0f4f8", fg("white")
      width=12, cursor="hand2",
      relief="flat",
      command=self.inserir
    )
    self.btn_limpar.pack
   
   
    # ========== LISTA DE ITENS (TREEVIEW) =========
    frame_lista = tk.Frame(self.root, bg="#f0f4f8")
    frame_lista.pack(pady=10, padx=20, fill="both", expand=True)
   
    # Scrollbar
    scrollbar = tk.Scrollbar(frame_lista)
    scrollbar.pack(side="right", fill="y")
   
    # Treeview
    colunas = ("descricao", "quantidade", "preco", "subtotal")
    self.tree = ttk.Treeview(
        frame_lista,
        show= "headings",
        yscrollcommand=scrollbar.set,
        height=10
    )
    scrollbar.config(command=self.tree.yview)
   
    # Configurar colunas
    self.tree.heading("descricao", text="Descrição")
    self.tree.heading("quantidade", text="0td")
    self.tree.heading("preco", text="Preço Unit. (R$)")
    self.tree.heading("subtotal", text="Subtotal (R$)")
   
    self.tree.column("descricao", widht=250, anchor="W")
    self.tree.column("quantidade", widht=60, anchor="center")
    self.tree.column("preco", widht=120, anchor="e")
    self.tree.column("subtotal", widht=120, anchor="e")
   
    self.treee.pack(fill)
   
    # Evento da seleçao
    self.tree.bind("<<TreeviewSelect>>", self.on_select)
   
    # ========= TOTAL =========
    frame_total = tk.Frame(self.root, bg="#f0f4f8")
    frame_total.pack(pady=10, padx=20, fill="X")
   
    self.lbl_total = tk.Label(
        frame_total,
        text="TOTAL: R$ 0,00",
        font=("Arial", 16, "bold"),
        bg="#f0f4f8",
        fg="#1a5276",
    )
    self.lbl_total.pack(side="right")
   
    # ======== STATUS BAR =========
    self.lbl_status = tk.Label(
        self.root,
        text="pronto. Selecione um item para editar ou deletar.",
        font=("Arial", 9),
        bg="#d5dbdb"
        fg="#2c3e50",
        anchor="W"
    )
    self.lbl_status.pack(fill="X", side="botton")

    # Estilo Treeview
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", font=("Arial", 10), rowheight=25)
    style.configure("Treeview.Heading", font=("Arial", 11, "bold"),background="#3498db", foreground="white")
    style.map("Treeview", background=[("selected", "#aed6f1")])

def on select(self, event):
    """Quando um item da lista é selecionado, preenche os campos"""
    selecao = self.tree.slection()
    if selecao:
        item_id = selecao[0]
        valores  = self tree.item(item_id, "values")

        self.txt_descricao.delete(0, tk.END)
        self.txt_descricao.insert(0, valores[0])

        self.txt_quantidade.delete(0, tk.END)
        self.txt_quantidade.insert(0, valores[1])

        self.txt_preço.delete(0, tk.END)
        self.txt_preço.insert(0, valores[2]. replace("R$", "").replace(".", "").replace(",", ""))

        self.item_selecionado = item_id
        self.lbl_status.config(text=f"Item delecionado: {vaçores[0]}")

def limpar_campos(self):
    """Limpar todos os campos de entrada"""
    self.txt_descrição.delete(0, tk.END)
    self.txt_quantidade.delete(0, tk.END)
    self.txt_preço.delete(0, tk.END)
    self.item_selecionado = None
    self.tree.seletion_remove(self.tree.selection())
    self.lbl_status.config(text="Campos limpos. Pronto para inserir novo item.")
    self.txt_descricao.focus()

def validar_entrada(self):
    """Valida os campos de entrada"""
    descricao = self.txt_descricao.get().strip()
    quantidade = self.txt_quantidade.get().strip()
    preco = self.txt_preco.get().strip()

    if not descricao:
        messagebox.showwarning("Aviso", "Digite a descrição de item!")
        return None

    try:
        qtd = float(quantidade.replace(",", ","))
        if qtd <= 0:
            messagebox.showwarning("Aviso", "Quantidade deve ser maior que zero!")
            return None
    except ValueError:
        messagebox.showwarning("Aviso", "Quantidade inváçida!")
        return None

    try:
        prc = float(preco.replace(",", ","))
        if pr < 0:
            messagebox.showwarning("Aviso", "Preço não pode ser negativo!")
        return None
    except ValueError:
        messagebox.showwarning("Aviso", "Preço inválido!")
        return None

    return ("descricao": descricao, "quantidade": qtd, "preco": prc)

def inserir(self):
    """Insere um novo item na lista"""
    dados = self.validar_entrada()
    if not dados:
        return

    self.itens.append(dados)
    self.salvar_no_arquivo()
    self.atualizar_lista()
    self.limpar_campos()
    self.lbl_status.config(text=f"Item '{dados['descricao']}' inserido com sucesso!")
    messagebox.showinfo("Sucesso", f"item'{dados['descricao']}'inserdo!")

def editar(self):
    """Editar o item selecionado"""
    if not self.item_selecionado:
        messagebox.showwarning("Aviso", "Selecione um item na lista para editar!")
        return

    dados = self.validar_entrada()
    if not dados:
        return

    # Encontrar o índice do item selecionado
    idx = self.tree.index(self.item_selecionado)
    self.itens = self.itens[idx = dados]

    self.salvar no arquivo()
    self.atualizar_lista()
    self.limpar_campos()
    self.lbl_status.config(text=f"Item '{dados['descricao']}' atualizado!")
    messagebox.showwarning("Aviso", "Selecione um item na lista para deletar!")

def deletar(self):
    """Deleta o item selecionado"""
    if not self.item_selecionado:
        messagebox.showwarning("Aviso", "selecione um item na lista para deletar!")
        return

    idx = self.tree.index(self.item_selecionado)
    item_nome = self.itens[idx]["descricao"]

    if messagebox.askyesno("Confirmar", f"Deseja realmente deletar '{item_nome}'?"):
        self.itens.pop(idx)
        self.salvar_no_arquivo()
        self.atualizar_lista()
        self.limpar_campos()
        self.lbl_status.config(text=f"Item '{item_nome}' deletado.")
        messagebox.showinfo("Sucesso", f"Item '{item_nome}' removido!")

def atualizar_lista(self):
    """Atualizar a Treeview com os dados da lista""" 
    # Limpar lista
    for item in self.tree.get_children():
        self.tree.delete(item)

    total = 0.0

    for item in self.itens:
        subtotal = item["quantidade"] * item["preco"]
        total += subtotalself.tree.insert("", "end", values=(
            
        ))
