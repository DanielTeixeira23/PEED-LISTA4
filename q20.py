def lista():
    dicionario = {}
    
    qnt = int(input('Quantas chaves vão ser adicionada? '))
    for i in range(qnt):
        chave = input(f'Digite o nome do {i+1}° aluno: ' )
        valor = float(input(f'Digite a nota do {i+1}° aluno: '))
        dicionario[chave] = valor
    
    maior_nota = max(dicionario.values())
    print('Nota maior: ')
    nota = {aluno: nota for aluno, nota in dicionario.items() if nota == maior_nota}          

    return nota

x = lista()
print(x)