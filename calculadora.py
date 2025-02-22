import tkinter as tk

# Função para adicionar o valor ao campo de exibição
def adicionar_valor(valor):
    display.insert(tk.END, valor)

# Função para calcular o resultado
def calcular():
    try:
        resultado = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Erro")

# Função para limpar o campo de exibição
def limpar():
    display.delete(0, tk.END)

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")

# Campo de exibição
display = tk.Entry(janela, font=("Arial", 20), justify="right")
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
        botao = tk.Button(janela, text=valor, font=("Arial", 16), command=calcular)
    else:
        botao = tk.Button(janela, text=valor, font=("Arial", 16), command=lambda v=valor: adicionar_valor(v))
    botao.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")

# Botão de limpar
botao_limpar = tk.Button(janela, text="C", font=("Arial", 16), command=limpar)
botao_limpar.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Ajustar o redimensionamento das células da grade
for i in range(6):
    janela.grid_rowconfigure(i, weight=1)
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

# Iniciar o loop principal da interface gráfica
janela.mainloop()