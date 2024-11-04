#Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.

list = []

#ler os numeros da lista
print('digite 5 números.')
for i in range(1, 6):
    num = int(input(f"digite o {i} número: "))
    list.append(num)

#mostrar o números com a sua posição na lista
print('a lista é:', list )
for i, p in enumerate(list):
    print(f'índice {i} => {p}')    