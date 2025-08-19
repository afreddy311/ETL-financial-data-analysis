import pandas as pd
import matplotlib.pyplot as plt

# Graficas de Barras de Gastos Mensuales por Categoría
df = pd.read_csv('data/resumen_gastos_mensual.csv')
plt.figure(figsize=(12, 6))
for category in df['category'].unique():    
    subset = df[df['category'] == category]
    plt.plot(subset['month'], subset['total_amount'], marker='o', label=category)
plt.title('Gastos Mensuales por Categoría')
plt.xlabel('Mes')  
plt.ylabel('Gasto Total')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('output/gastos_mensuales_por_categoria.png')  
plt.show()

# Grafico circular de un mes específico
mes = '2024-06'
df_mes = df[df['month'] == mes]

plt.figure(figsize=(6, 6))
plt.pie(df_mes['total_amount'], labels=df_mes['category'], autopct='%1.1f%%', startangle=90)
plt.title(f'Distribucion de gastos en {mes}')
plt.savefig(f'output/distribucion_gastos_{mes}.png')
plt.show()

