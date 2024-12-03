from cachorro import Cachorro
from gato import Gato
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Lista para armazenar os animais cadastrados
lista = []

# Função de criação de objetos
def cadastrarAnimal():
    nome = entryNome.get()
    idade = entryIdade.get()
    porte = entryPorte.get()
    raca = entryRaca.get()
    tipo = varTipo.get()

    # Verificar campos obrigatórios de acordo com o tipo de animal
    if not nome:
        messagebox.showinfo("Erro", "O nome deve ser preenchido")
        return
    if not idade:
        messagebox.showinfo("Erro", "A idade deve ser preenchida")
        return

    if tipo == "Cachorro":
        if not porte:
            messagebox.showinfo("Erro", "O porte deve ser preenchido para Cachorros")
            return
    elif tipo == "Gato":
        if not raca:
            messagebox.showinfo("Erro", "A raça deve ser preenchida para Gatos")
            return

    # Criar o objeto de acordo com o tipo selecionado
    if tipo == "Cachorro":
        c = Cachorro(nome, idade, porte)
        salvar(c)
    else:
        g = Gato(nome, idade, raca)
        salvar(g)

    # Mensagem de sucesso
    messagebox.showinfo("Cadastro", f"{tipo} cadastrado com sucesso!")

    # Limpar os campos após o cadastro
    entryNome.delete(0, tk.END)
    entryIdade.delete(0, tk.END)
    entryPorte.delete(0, tk.END)
    entryRaca.delete(0, tk.END)

# Função para salvar o objeto na lista
def salvar(obj):
    lista.append(obj)

# Função para atualizar a Listbox
def atualizarListbox():
    listbox.delete(0, tk.END)  # Limpar a listbox
    for obj in lista:
        listbox.insert(tk.END, obj.mostrar())  # Inserir os objetos na listbox

# Função para alternar campos de entrada com base no tipo de animal
def alternarCampos():
    if varTipo.get() == "Cachorro":
        entryPorte.config(state="normal")
        entryRaca.config(state="disabled")
    else:
        entryPorte.config(state="disabled")
        entryRaca.config(state="normal")

# Criar a janela principal
janela = tk.Tk()
janela.title("Cadastro de Animais")
janela.geometry("600x300")

# Criar o notebook
janelinha = ttk.Notebook(janela)
janelinha.pack(fill="both", expand=True)

# Criar as abas
aba1 = ttk.Frame(janelinha)
aba2 = ttk.Frame(janelinha)

# Adicionar abas ao Notebook
janelinha.add(aba1, text="Cadastro")
janelinha.add(aba2, text="Lista")

# Configurar widgets dentro da aba1
label1 = tk.Label(aba1, text="Nome", font=("", 15))
label1.grid(row=0, column=0, sticky="w", padx=10, pady=5)

entryNome = tk.Entry(aba1, font=("", 15))
entryNome.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

label2 = tk.Label(aba1, text="Idade", font=("", 15))
label2.grid(row=1, column=0, sticky="w", padx=10, pady=5)

entryIdade = tk.Entry(aba1, font=("", 15))
entryIdade.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

label3 = tk.Label(aba1, text="Porte", font=("", 15))
label3.grid(row=2, column=0, sticky="w", padx=10, pady=5)

entryPorte = tk.Entry(aba1, font=("", 15))
entryPorte.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

label4 = tk.Label(aba1, text="Raça", font=("", 15))
label4.grid(row=3, column=0, sticky="w", padx=10, pady=5)

entryRaca = tk.Entry(aba1, font=("", 15))
entryRaca.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

# Botões de rádio para selecionar tipo
tk.Label(aba1, text="Animal", font=("", 15)).grid(row=4, column=0, sticky="w", padx=10, pady=5)

varTipo = tk.StringVar(value="Cachorro")
tk.Radiobutton(aba1, text="Cachorro", font=15, variable=varTipo, value="Cachorro", command=alternarCampos).grid(row=4, column=1, sticky="w", padx=15, pady=5)
tk.Radiobutton(aba1, text="Gato", font=15, variable=varTipo, value="Gato", command=alternarCampos).grid(row=4, column=2, sticky="w", padx=15, pady=5)

tk.Button(aba1, text="Cadastrar", font=("", 15), command=cadastrarAnimal).grid(row=5, columnspan=2)

# Lista
listbox = tk.Listbox(aba2)
listbox.config(font=("", 15))
listbox.grid(row=0, column=0, sticky="nsew", padx=15, pady=10)

# Botão de atualização
tk.Button(aba2, text="Atualizar", font=("", 15), command=atualizarListbox).grid(row=1, column=0)

# Configuração para que a Listbox e o botão se ajustem ao tamanho da janela
aba2.grid_rowconfigure(0, weight=1)
aba2.grid_columnconfigure(0, weight=1)

# Executar o loop principal da aplicação
janela.mainloop()
