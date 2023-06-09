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

def lista_numeros():
    f = Fila()
    
    num = 0
    print('Digite um número negativo para parar.')
    while num >= 0:
        if num>= 0:
            num = int(input('Digite um número: '))
            f.adicionar(num)
       
    print('Números na ordem em que foram adicionados:')
    while not f.is_empty():
        print(f.remover(), end=' ')
    
    return f
    
ordem = lista_numeros()