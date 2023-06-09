def lista_numeros():
    numeros = []
    
    soma = 0
    qnt = int(input('Quantos número vão ser adicionados: '))
    for i in range(qnt):
        num = int(input(f'Digite o {i+1}° número: '))
        soma+= num
        
    numeros.append(soma)
    return numeros 
    
soma_lista = lista_numeros()
print('Soma:', soma_lista)