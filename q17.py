def frase():
    lista = []
    
    for i in range(5):
        palavra = input(f'Digite a {i+1}° palavra: ')
        lista.append(palavra)
    
    lista_caracter = []
    for palavra in lista:
        if len(palavra) > 5:
            lista_caracter.append(palavra)
            
    return lista_caracter

maior_palavra = frase()
print('Palavra com mais de 5 caracteres:', maior_palavra)