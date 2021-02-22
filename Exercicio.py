escolaridade=float(input("Quantos anos de estudo?"))
if escolaridade < 1:
    print('Iniciante')
elif escolaridade < 3:
    print('Intermediário')
elif escolaridade <= 6:
    print('Avançado')
else:
    print('Jedi Master')