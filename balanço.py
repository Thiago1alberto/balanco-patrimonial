from decimal import Decimal, InvalidOperation
import tkinter as tk
from tkinter import simpledialog, messagebox

class BalancoPatrimonialApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Balanço Patrimonial")
        self.master.geometry("400x300")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.ativo_label = tk.Label(self, text="Ativos:")
        self.ativo_label.pack(side="top")
        self.ativo_valor = tk.Label(self, text="0.00")
        self.ativo_valor.pack(side="top")
        self.ativo_button = tk.Button(self, text="Adicionar valor de Ativo", command=self.add_ativo, width=30)
        self.ativo_button.pack(side="top")

        self.passivo_label = tk.Label(self, text="Passivos:")
        self.passivo_label.pack(side="top")
        self.passivo_valor = tk.Label(self, text="0.00")
        self.passivo_valor.pack(side="top")
        self.passivo_button = tk.Button(self, text="Adicionar valor de Passivo", command=self.add_passivo, width=30)
        self.passivo_button.pack(side="top")

        self.patrimonio_label = tk.Label(self, text="Patrimônio Líquido:")
        self.patrimonio_label.pack(side="top")
        self.patrimonio_valor = tk.Label(self, text="0.00")
        self.patrimonio_valor.pack(side="top")
        self.patrimonio_button = tk.Button(self, text="Adicionar valor de Patrimônio Líquido", command=self.add_patrimonio, width=30)
        self.patrimonio_button.pack(side="top")

        self.quit = tk.Button(self, text="Fechar", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def add_ativo(self):
        descricao, valor = self.get_descricao_valor("Ativo")
        atual = Decimal(self.ativo_valor["text"])
        novo = atual + valor
        self.ativo_valor["text"] = str(novo)

    def add_passivo(self):
        descricao, valor = self.get_descricao_valor("Passivo")
        atual = Decimal(self.passivo_valor["text"])
        novo = atual + valor
        self.passivo_valor["text"] = str(novo)

    def add_patrimonio(self):
        descricao, valor = self.get_descricao_valor("Patrimônio Líquido")
        atual = Decimal(self.patrimonio_valor["text"])
        novo = atual + valor
        self.patrimonio_valor["text"] = str(novo)
        
    
    def get_descricao_valor(self, categoria):
        nova_janela = tk.Toplevel(self.master)
        nova_janela.title(f"Adicionar {categoria}")
        nova_janela.geometry("300x150")
        nova_janela.resizable(False, False)

        descricao_label = tk.Label(nova_janela, text="Descrição:")
        descricao_label.pack(side="top", padx=10, pady=10)
        descricao_entry = tk.Entry(nova_janela, width=30)
        descricao_entry.pack(side="top", padx=10)

        valor_label = tk.Label(nova_janela, text="Valor:")
        valor_label.pack(side="top", padx=10, pady=10)
        valor_entry = tk.Entry(nova_janela, width=10)
        valor_entry.pack(side="top", padx=10)

        confirmar_button = tk.Button(nova_janela, text="Confirmar", command=lambda: self.adicionar_descricao_valor(categoria, descricao_entry.get(), valor_entry.get(), nova_janela))
        confirmar_button.pack(side="top", padx=10, pady=10)
        confirmar_button.config(height=10)
        
    def adicionar_descricao_valor(self, categoria, descricao, valor, nova_janela):
        try:
            valor_decimal = Decimal(valor)
        except InvalidOperation:
            tk.messagebox.showerror("Valor inválido", "Valor inválido. Tente novamente.")
            return
        atual = Decimal(getattr(self, f"{categoria.lower()}_valor")["text"])
        novo = atual + valor_decimal
        getattr(self, f"{categoria.lower()}_valor")["text"] = str(novo)

        nova_janela.destroy()

    def get_valor(self, categoria):
        while True:
            valor_str = tk.simpledialog.askstring("Inserir valor", f"Insira o valor de {categoria}:")
            try:
                valor = Decimal(valor_str)
                return valor
            except InvalidOperation:
                tk.messagebox.showerror("Valor inválido", "Valor inválido. Tente novamente.")
                
    def calcular_balanco(self):
        ativo = Decimal(self.ativo_valor["text"])
        passivo = Decimal(self.passivo_valor["text"])
        patrimonio = Decimal(self.patrimonio_valor["text"])
        if ativo == passivo + patrimonio:
            tk.messagebox.showinfo("Balanço Patrimonial", "Balanço Patrimonial correto!")
        else:
            diferenca = ativo - (passivo + patrimonio)
            tk.messagebox.showwarning("Balanço Patrimonial", f"Balanço Patrimonial incorreto!\nDiferença: {diferenca}")

root = tk.Tk()
app = BalancoPatrimonialApp(master=root)
app.mainloop()