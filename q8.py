class Item:
   def __init__(self, valor):
       self.valor = valor
       self.prox = None
    
class ListaEncadeadaSimples:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
        
    def is_empty(self):
        return self.inicio is None
    
    def adicionar_inicio(self, valor):
        novo_item = Item(valor)
        novo_item.prox = self.inicio
        self.inicio = novo_item
        self.tamanho += 1

    def adicionar_fim(self, valor):
        novo_item = Item(valor)
        if self.is_empty():
            self.inicio = novo_item
        else:
            atual = self.inicio
            while atual.prox is not None:
                atual = atual.prox
            atual.prox = novo_item
        self.tamanho += 1
        
    def remover_inicio(self):
        if self.is_empty():
            raise Exception('A lista está vazia.')
        else:
            self.inicio = self.inicio.prox
        self.tamanho -= 1
          
    def remover_fim(self):
        if self.is_empty():
            raise Exception('A lista está vazia.')
        elif self.inicio.prox is None:
            self.inicio = None
            self.tamanho -= 1
        else:
            atual = self.inicio
            anterior = None
            while atual.prox is not None:
                anterior = atual
                atual = atual.prox
            anterior.prox = None
            self.tamanho -= 1
    
    def buscar(self, elemento):
        if self.inicio is None:
            raise Exception('A lista está vazia.')
        atual = self.inicio
        
        while atual is not None:
            if atual.valor == elemento:
                return True
            atual = atual.prox
        return False
    
    def listar(self):
        if self.inicio is None:
            raise Exception('A lista está vazia.')
        atual = self.inicio
        while atual is not None:
            print(atual.valor, end=' ')
            atual = atual.prox
    
    def obter_tamanho(self):
        return self.tamanho
    
def ordem():
    l = ListaEncadeadaSimples()
    lista = []
    
    qnt = int(input('Quantos número vão ser adicionados: '))
    for i in range(qnt):
        num = int(input(f'Digite o {i+1}° número: '))
        lista.append(num)
    
    for num in reversed(lista):
        l.adicionar_fim(num)
        
    return l

lista_inversa = ordem()
print('Lista inversa:')
lista_inversa.listar()