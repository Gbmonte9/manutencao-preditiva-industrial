import os
import matplotlib.pyplot as plt
import seaborn as sns
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder \
    .appName("EDA_Manutencao_Preditiva_Iane") \
    .getOrCreate()

print("✅ Sessão PySpark pronta para a Análise Exploratória!")

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
caminho_sensores = os.path.join(DIRETORIO_ATUAL, "../data/base_sintetica_manutencao_preditiva/sensores.csv")

df_sensores = spark.read.csv(caminho_sensores, header=True, inferSchema=True)

print("\n--- 📊 Resumo Estatístico Geral dos Sensores ---")
df_sensores.select(
    "temperatura_c", "vibracao_mm_s", "pressao_bar", "corrente_a", "rotacao_rpm"
).describe().show()

print("\n--- ⚠️ Contagem de Falhas (0 = Operação Normal, 1 = Falha) ---")
df_sensores.groupBy("falha", "nivel_risco").count().orderBy("count", ascending=False).show()

print("\n--- 🏭 Médias Operacionais por Máquina ---")
df_maquinas = df_sensores.groupBy("machine_id").agg(
    F.round(F.avg("temperatura_c"), 2).alias("med_temp"),
    F.round(F.avg("vibracao_mm_s"), 2).alias("med_vibracao"),
    F.sum("falha").alias("total_falhas")
).orderBy("machine_id").toPandas()

caminho_pasta_figuras = os.path.join(DIRETORIO_ATUAL, "../docs/figuras")
os.makedirs(caminho_pasta_figuras, exist_ok=True)
sns.set_theme(style="darkgrid")

fig, ax1 = plt.subplots(figsize=(12, 5))

color = 'tab:red'
ax1.set_xlabel('Máquina (machine_id)')
ax1.set_ylabel('Temperatura Média (°C)', color=color)
ax1.bar(df_maquinas['machine_id'], df_maquinas['med_temp'], color=color, alpha=0.6)
ax1.tick_params(axis='y', labelcolor=color)
plt.xticks(rotation=45)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Total de Falhas Registradas', color=color)
ax2.plot(df_maquinas['machine_id'], df_maquinas['total_falhas'], color=color, marker='o', linewidth=2)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Iane Alimentos - Temperatura Média e Ocorrência de Falhas por Equipamento')
fig.tight_layout()
caminho_fig1 = os.path.join(caminho_pasta_figuras, "eda_temperatura_falhas.png")
plt.savefig(caminho_fig1, dpi=300)
plt.close()

print(f"✅ Gráfico salvo com sucesso em: {caminho_fig1}")