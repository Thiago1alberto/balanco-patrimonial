import tkinter as tk
from decimal import Decimal, InvalidOperation
from tkinter import messagebox

class BalançoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Balanço Patrimonial")

        # Cria os rótulos e campos de entrada para as categorias
        self.ativos = []
        ativos_label = tk.Label(master, text="Ativos:")
        ativos_label.grid(row=0, column=0)
        self.ativos_entry = tk.Entry(master)
        self.ativos_entry.grid(row=0, column=1)

        self.passivos = []
        passivos_label = tk.Label(master, text="Passivos:")
        passivos_label.grid(row=1, column=0)
        self.passivos_entry = tk.Entry(master)
        self.passivos_entry.grid(row=1, column=1)

        self.receitas = []
        receitas_label = tk.Label(master, text="Receitas:")
        receitas_label.grid(row=2, column=0)
        self.receitas_entry = tk.Entry(master)
        self.receitas_entry.grid(row=2, column=1)

        self.despesas = []
        despesas_label = tk.Label(master, text="Despesas:")
        despesas_label.grid(row=3, column=0)
        self.despesas_entry = tk.Entry(master)
        self.despesas_entry.grid(row=3, column=1)

        # Cria os botões para adicionar valores às categorias
        ativos_button = tk.Button(master, text="Adicionar Ativo", command=self.adicionar_ativo)
        ativos_button.grid(row=0, column=2)

        passivos_button = tk.Button(master, text="Adicionar Passivo", command=self.adicionar_passivo)
        passivos_button.grid(row=1, column=2)

        receitas_button = tk.Button(master, text="Adicionar Receita", command=self.adicionar_receita)
        receitas_button.grid(row=2, column=2)

        despesas_button = tk.Button(master, text="Adicionar Despesa", command=self.adicionar_despesa)
        despesas_button.grid(row=3, column=2)

        # Cria o botão para calcular o balanço
        calcular_button = tk.Button(master, text="Calcular", command=self.calcular_balanço)
        calcular_button.grid(row=4, column=1)

    def adicionar_valor(self, lista, entry):
        lista.append(entry.get())
        entry.delete(0, tk.END)

    def adicionar_ativo(self):
        self.adicionar_valor(self.ativos, self.ativos_entry)
        self.ativos_entry.focus()

    def adicionar_passivo(self):
        self.adicionar_valor(self.passivos, self.passivos_entry)
        self.passivos_entry.focus()

    def adicionar_receita(self):
        self.adicionar_valor(self.receitas, self.receitas_entry)
        self.receitas_entry.focus()

    def adicionar_despesa(self):
        self.adicionar_valor(self.despesas, self.despesas_entry)
        self.despesas_entry.focus()

    def calcular_balanço(self):
        ativos = self.get_valor_total(self.ativos)
        passivos = self.get_valor_total(self.passivos)
        receitas = self.get_valor_total(self.receitas)
        despesas = self.get_valor_total(self.despesas)

        patrimonio_liquido = ativos - passivos
        resultado = receitas - despesas

        messagebox.showinfo("Resultado", f"Patrimônio líquido: {patrimonio_liquido}\nResultado: {resultado}", parent=self.master)

    def adicionar_valor(self, lista, entry):
        lista.append(entry.get())
        entry.delete(0, tk.END)

    def adicionar_ativo(self):
        self.adicionar_valor(self.ativos, self.ativo_entry)

if __name__ == '__main__':
    root = tk.Tk()
    BalançoGUI(root)
    root.mainloop()