import os
import matplotlib.pyplot as plt
import numpy as np #Usar numpy para criar arrays
from utils import salvar_grafico_sequencial

# 1. Configuração inicial 
fig = plt.figure(figsize=(10, 8)) #Cria a figura + tamanho
ax =  fig.add_subplot(111, projection='3d') #prijection=3d -> define que os eixos serão 3d

# 2. Geração de dados de exemplo
np.random.seed(42) #P/ resultados reproduzíveis
n = 100 #Número de pontos

# Substituir por valores reais (dados aleatórios)
x = np.random.rand(n) * 10
y = np.random.rand(n) * 5
z = np.random.rand(n) * 8

# 3. Criação do gráfico de dispersão 3D
scatter = ax.scatter(x, y, z, c=z, cmap='viridis', s=50, alpha=0.7, edgecolors='w')
#c=z -> Cores baseadas no eixo Z
#s=50 -> Tamanho dos pontos
#alpha=0.7 -> Transparência dos pontos
#edgecolors='w' -> Borda branca nos pontos

# 4. Personalização
ax.set_xlabel('Eixo X', fontsize=12) #Rótulo do eixo X + tamanho da fonte
ax.set_ylabel('Eixo Y', fontsize=12) #Rótulo do eixo Y + tamanho da fonte
ax.set_zlabel('Eixo Z', fontsize=12) #Rótulo do eixo Z + tamanho da fonte
ax.set_title('Gráfico de Dispersão 3D (Treinamento)', fontsize=16) #Título do gráfico + tamanho da fonte
#ax.set_xlim([0, 12]) #Limite do eixo X
# ax.set_ylim([0, 6]) #Limite do eixo Y
# ax.set_zlim([0, 10]) #Limite do eixo Z (PODE BOTAR QUALQUER VALOR NOS 3)

# 5. Barra de Cores
cbar = fig.colorbar(scatter, ax=ax, pad=0.1) #Barra de cores
cbar.set_label('Intensidade (Z)', rotation=270, labelpad=15, fontsize=12) #Rótulo da barra de cores + rotação + espaçamento + tamanho da fonte

# 6. Ajuste de perspectiva
ax.view_init(elev=25, azim=35) #Ângulo de visualização

# 7. Salvar figura (Opcional)
#plt.savefig('grafico_3d_teste.png', dpi=300) #(OPÇÃO BÁSICA DE SALVAR)
salvar_grafico_sequencial(base_dir="Dispersão PNGs") #Função que eu criei
#Se eu tirar base_dir="Dispersão PNGs" de dentro do (), ele vai criar uma pasta chamada outputs

# 8. Exibir gráfico
plt.tight_layout() #Ajuste automático do layout
plt.show() #Exibir o gráfico