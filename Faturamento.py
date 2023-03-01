import json

with open("dados.json", "r") as f:
    faturamento_mensal = json.load(f)

faturamento_mensal = {faturamento_diario['dia']:faturamento_diario['valor'] for faturamento_diario in faturamento_mensal if faturamento_diario['valor'] > 0}

faturamento_minimo = min(faturamento_mensal, key=faturamento_mensal.get)
faturamento_maximo = max(faturamento_mensal, key=faturamento_mensal.get)

print(f'O menor faturamento ocorreu no dia {faturamento_minimo} e foi de R$ {faturamento_mensal[faturamento_minimo]:.2f}')
print(f'O maior faturamento ocorreu no dia {faturamento_maximo} e foi de R$ {faturamento_mensal[faturamento_maximo]:.2f}')

media = faturamento_mensal.values()
media = sum(media) / len(media)
dias_faturamento_acima_media = 0

for faturamento in faturamento_mensal.values():
    if faturamento > media:
        dias_faturamento_acima_media += 1

print(f'Neste mês, {dias_faturamento_acima_media} dias tiveram faturamento acima da média mensal.')
