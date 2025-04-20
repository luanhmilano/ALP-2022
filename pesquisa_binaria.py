'''
import math

def calcular_volume_esfera(raio):
    volume = (4/3) * math.pi * (raio ** 3)
    return volume

raio = int(input("digite o raio: "))
volume = calcular_volume_esfera(raio)
print(f"O volume da esfera é {volume} com o raio {raio}")'''

def calcular_media(notas, tipo):
    if tipo == 'A':
        media = sum(notas) / len(notas)
    elif tipo == 'P':
        pesos = [5, 3, 2]
        soma_pon = sum(nota * peso for nota, peso in zip(notas, pesos))
        soma_pes = sum(pesos)
        media = soma_pon / soma_pes
    elif tipo == 'H':
        inver = [1 / nota for nota in notas]
        media = len(notas) / sum(inver)

    return media

notas = []
for i in range(3):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)
tipo = input("Digite o tipo de média desejada, sendo \nA - aritmética\nP - ponderada\nH - harmônica: ").lower()

media_calculada = calcular_media(notas, tipo)
print(f"A média calculada é {media_calculada}")
