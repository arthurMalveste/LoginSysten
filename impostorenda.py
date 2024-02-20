carros = ['Vectra', 'Astra', 'Palio', 'Salveiro', 'Maserati']

def mos():
    for idx in range(len(carros)):
        print(f'{idx}, {carros[idx]}')

rmv = int(input(f'Deseja remover qual carro ?'))

del carros[rmv]
mos()

add = input(f'Qual carro gostaria de adicionar?')

carros.append(add)
mos()