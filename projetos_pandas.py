import pandas as pd
import io
company_data = "Produto,Preco,Quantidade\nTlecado,150.0,2\nMonitor,350.0,1\nMouse,80.0,3\nHeadset,220.0,2"
df_empresa = pd.read_csv(io.StringIO(company__data))
df_empresa["Faturamento"] = df_empresa["Preco"] * df_empresa["Quantidade"]
print("--- Tabela Completa de Vendas ---")
print(df_empresa)
total_geral = df_empresa["Faturamento"].sum()
media_geral = df_empresa["Faturamento"].mean()
print("\nTotal Revenue: $" + str(total_geral))
print("\nAverage Revenue: $" + str(media_geral))
filter_high_value = df_empresa["Faturamento"] > 300.0
high_value_products = df_empresa[filter_high_value]
print(\n--- High Value Products ---")
print(high_value_products)

dados_vendas = "Cliente,Valor\nNatanael,150.0\nCarlos,200.0\nAmanda,\nBruno,100.0"
df_vendas = pd.read_csv(io.StringIO(dados_vendas))

media_valores = df_vendas["Valor"].mean()
df_vendas_media = df_vendas.fillna(media_valores)
print("\n--- Planilha de Vendas Tratada com a Media ---")
print(df_vendas_media)

def analisador_de_vendas(dados_brutos, nome_projeto):
    df = pd.read_csv(io.StringIO.(dados_brutos))
    media = df["Faturamento"].mean()
    df_limpo = df.fillna(media)
    fig, ax = plt.subplots(figsize=(7, 4))
    barras = ax.bar(df_limpo["Produto"], df_limpo["Faturamento"], color="purple")
    ax.bar_label(barras, padding=3, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    plt.title("Relatorio Automatizado: " + nome_projeto, fontsize=12, fontsize="bold)
    plt.show()
planilha_loja = "Produto,Faturamento\nTeclado,300.0\nMonitor,\nMouse,240.0\nHeadset,440.0"
analisador_de_vendas(planilha_loja, "Loja do Natanael")
