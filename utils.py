#Solução contador para salvar gráficos sequencialmente
#Contador é recalculado a cada execução, baseado nos arquivos existentes no diretório
#Começa em 1. Se tiver um arquivo 1, ele salva como 2 em diante
import os
import matplotlib.pyplot as plt
from pathlib import Path

def salvar_grafico_sequencial(base_dir="outputs", prefixo="grafico"):
    Path(base_dir).mkdir(exist_ok=True) #Cria o diretório se não existir
    contador=1
    while True:
        nome_arquivo = f"{prefixo}_{contador}_3d_teste.png"
        caminho = os.path.join(base_dir, nome_arquivo)
        if not os.path.exists(caminho):
            break
        contador += 1
    plt.savefig(caminho, dpi=300) #Salva o gráfico c/ resolução de 300 dpi
    print(f"Gráfico salvo como: {caminho}")

