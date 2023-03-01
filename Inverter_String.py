string_para_inverter = input("Digite a string que deseja inverter: ")
string_invertida = ""
i = len(string_para_inverter) - 1

while i>=0:
    string_invertida += string_para_inverter[i]
    i-=1

print(f'A string invertida é: {string_invertida}')