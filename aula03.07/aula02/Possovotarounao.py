print('Vamos votar em um time')
nome = input ('digite seu nome')
valor = int (input('digite o numero do voto;'))
if (valor<=1):
    print(f'{nome} votou em Branco')
if (valor>=3):
    print(f'{nome} Cancelou seu Voto')
elif (valor==2):
    print(f'{nome}, seu voto foi Confirmado')
else:
    print(f'{nome} Você voto foi cancelado')