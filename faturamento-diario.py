import json

# Lê o arquivo JSON que contém os dados de faturamento diário da distribuidora
with open('dados.json') as f:
    dados = json.load(f)

# Extrai apenas os valores de faturamento do dicionário para uma lista
valores = [dado['valor'] for dado in dados]

# Calcula o menor valor de faturamento ocorrido em um dia do mês
menor_faturamento = min(valores)

# Calcula o maior valor de faturamento ocorrido em um dia do mês
maior_faturamento = max(valores)

# Calcula a média mensal de faturamento, ignorando os dias sem faturamento
faturamento_total = sum(dado['valor'] for dado in dados if dado['valor'] > 0)
dias_com_faturamento = len([dado for dado in dados if dado['valor'] > 0])
media_faturamento = faturamento_total / dias_com_faturamento

# Calcula o número de dias no mês em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = len([dado for dado in dados if dado['valor'] > media_faturamento])

# Imprime os resultados
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Média mensal de faturamento: {media_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
