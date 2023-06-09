def lista_numeros():
    primeira_lista = []
    segunda_lista = []
    
    elementos_comuns = []
    
    print('Digite os números da primeira lista.')
    for i in range(5):
        num = int(input(f'Digite o {i+1}° número: '))
        primeira_lista.append(num)
        
    print('\nDigite os números da segunda lista.')
    for i in range(5):
        num = int(input(f'Digite o {i+1}° número: '))
        segunda_lista.append(num)
    
    for num in primeira_lista:
        if num in segunda_lista:
            elementos_comuns.append(num)
    
    return elementos_comuns

lista = lista_numeros()
print('Elementos em comum:', lista)