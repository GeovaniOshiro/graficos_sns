import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

#Função para carregar dados e gerar gráficos
def carregar_dados():
    #arregar dados do arquivo Excel
    file_path = filedialog.askopenfilename()
    df = pd.read_excel(file_path)
    
    # Gerar gráfico de barras: ------
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='Categoria',y='Valor1')
    plt.title('Gráfico de Barras')
    plt.xlabel('Categoria')
    plt.ylabel('Valor1')
    plt.show()
    
    # Crie o gráfico de linha: -------
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='Categoria', y='Valor1')
    plt.title('Gráfico de Linhas')
    plt.xlabel('Categoria')
    plt.ylabel('Valores')
    plt.show()
    
    # 3D
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df['Valor1'], df['Valor2'], df['Valor3'], c='r', marker='o')
    ax.set_title('Gráfico 3D')
    ax.set_xlabel('Valor1')
    ax.set_ylabel('Valor2')
    ax.set_zlabel('Valor3')
    plt.show()
    
    # Exibir estatísticas básicas
    estatisticas = df.describe()
    estatisticas_text.delete('1.0', tk.END)
    estatisticas_text.insert(tk.END, estatisticas)

# Criar janela principal
root = tk.Tk()
root.title("Dashboard de Dados")
root.geometry("800x600")

# Adicionar botão para carregar dados
btn_carregar = tk.Button(root, text="Carregar Dados", command=carregar_dados, bg='#4CAF50', fg='white', font=('Helvetica', 12, 'bold'))
btn_carregar.pack(pady=20)

# Adicionar área para exibir estatísticas
estatisticas_frame = tk.LabelFrame(root, text="Estatísticas Básicas", padx=10, pady=10, font=('Helvetica', 12, 'bold'))
estatisticas_frame.pack(padx=10, pady=10, fill="both", expand="yes")

estatisticas_text = tk.Text(estatisticas_frame, wrap=tk.WORD, height=10, font=('Helvetica', 10))
estatisticas_text.pack(fill="both", expand="yes")

# Rodar o aplicativo
root.mainloop()
