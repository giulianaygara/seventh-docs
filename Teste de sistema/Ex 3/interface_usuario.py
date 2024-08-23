import tkinter as tk
from tkinter import messagebox

class AplicativoSaudacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo de Saudação")

        self.label_nome = tk.Label(root, text="Digite seu nome:")
        self.label_nome.pack()

        self.entrada_nome = tk.Entry(root)
        self.entrada_nome.pack()

        self.botao_saudacao = tk.Button(root, text="Saudar", command=self.saudacao)
        self.botao_saudacao.pack()

        self.label_resultado = tk.Label(root, text="")
        self.label_resultado.pack()

    def saudacao(self):
        nome = self.entrada_nome.get()
        if nome:
            self.label_resultado.config(text=f"Olá, {nome}!")
        else:
            messagebox.showwarning("Aviso", "Por favor digite seu nome.")