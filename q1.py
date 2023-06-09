class Item:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        
    def is_empty(self):
        return self.inicio is None
    
    def adicionar(self, valor):
        novo_item = Item(valor)
        if self.is_empty():
            self.inicio = novo_item
            self.fim = novo_item
        else:
            self.fim.proximo = novo_item
            self.fim = novo_item
        self.tamanho += 1
        
    def remover(self):
        if self.is_empty():
            raise Exception('A pilha está vazia')
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return valor
    
    def obter_tamanho(self):
        return self.tamanho

def lista_num():
    f = Fila() 

    for i in range(5):
        num = int(input(f'Digite o {i+1}° número: '))
        f.adicionar(num)
    return f

ordem = lista_num()

while not ordem.is_empty():
    print('\n')
    print(f'Removendo elemento: {ordem.remover()}')
    if not ordem.is_empty():
        print(f'Próximo elemento: {ordem.inicio.valor}')
    else:
        print('Todos os elementos foram removidos.')