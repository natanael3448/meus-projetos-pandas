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
