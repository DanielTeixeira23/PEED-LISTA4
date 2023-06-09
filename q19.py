def frase():
    lista = []
    
    for i in range(3):
        palavra = input(f'Digite a {i+1}° palavra: ')
        lista.append(palavra)
    
    maior = ''
    for palavra in lista:
        if len(palavra) > len(maior):
            maior = palavra
            
    return maior

maior_palavra = frase()
print('Maior palavra:', maior_palavra)