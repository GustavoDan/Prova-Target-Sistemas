faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53,
}

faturamento_total = sum(faturamento_por_estado.values())

print('O percentual de faturamento de cada estado foi:')
for estado, faturamento in faturamento_por_estado.items():
    print(f"{estado} - {faturamento/faturamento_total*100:.2f}%")