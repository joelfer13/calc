import tkinter as tk
from tkinter import ttk

# Funções
def adicionar_valor(valor):
    display.insert(tk.END, valor)

def calcular():
    try:
        resultado = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Erro")

def limpar():
    display.delete(0, tk.END)

# Cores personalizadas
cor_fundo = "#2E3440"  # Azul escuro
cor_botoes = "#4C566A"  # Cinza azulado
cor_texto = "#ECEFF4"   # Branco gelo
cor_display = "#3B4252" # Cinza escuro

# Fontes personalizadas
fonte_display = ("Arial", 24)
fonte_botoes = ("Arial", 16)

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.configure(bg=cor_fundo)

# Aplicar o tema 'clam'
style = ttk.Style()
style.theme_use("clam")

# Campo de exibição
display = tk.Entry(janela, font=fonte_display, bg=cor_display, fg=cor_texto, justify="right", insertbackground=cor_texto)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Botões
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Posicionar os botões na janela
for i, valor in enumerate(botoes):
    linha = i // 4 + 1
    coluna = i % 4
    if valor == '=':
        botao = tk.Button(janela, text=valor, font=fonte_botoes, bg=cor_botoes, fg=cor_texto,
                          activebackground=cor_fundo, activeforeground=cor_texto, command=calcular)
    else:
        botao = tk.Button(janela, text=valor, font=fonte_botoes, bg=cor_botoes, fg=cor_texto,
                          activebackground=cor_fundo, activeforeground=cor_texto, command=lambda v=valor: adicionar_valor(v))
    botao.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")

# Botão de limpar
botao_limpar = tk.Button(janela, text="C", font=fonte_botoes, bg=cor_botoes, fg=cor_texto,
                         activebackground=cor_fundo, activeforeground=cor_texto, command=limpar)
botao_limpar.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Ajustar o redimensionamento das células da grade
for i in range(6):
    janela.grid_rowconfigure(i, weight=1)
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

# Iniciar o loop principal da interface gráfica
janela.mainloop()