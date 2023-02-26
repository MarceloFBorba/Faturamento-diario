Esse programa em Python recebe um dado em json que guarda o faturamento  diário de uma distribuidora, ele calcula e retorna os seguintes dados.
- O menor valor de faturamento ocorrido em um dia do mês;
- O maior valor de faturamento ocorrido em um dia do mês;
- Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

Explicação do codigo
- O arquivo dados.json é lido e armazenado na variável dados.
- Usando uma list comprehension, criamos uma lista contendo apenas os valores de faturamento da distribuidora.
- O menor valor de faturamento é calculado com a função min.
- O maior valor de faturamento é calculado com a função max.
- A média mensal de faturamento é calculada da mesma forma que no código anterior, com a diferença de que agora usamos dado['valor'] para acessar o valor de faturamento em cada item do dicionário.
 - O número de dias no mês em que o valor de faturamento diário foi superior à média mensal é calculado usando uma list comprehension semelhante à do código anterior.
