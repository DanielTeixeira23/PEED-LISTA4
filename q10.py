class Item:
   def __init__(self, valor):
       self.valor = valor
       self.prox = None
       self.ant = None
    
class ListaEncadeadaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        
    def is_empty(self):
        return self.inicio is None
    
    def adicionar_inicio(self, valor):
        novo_item = Item(valor)
        if self.is_empty():
            self.inicio = novo_item
            self.fim = novo_item
        else:
            novo_item.prox = self.inicio
            self.inicio.ant = novo_item
            self.inicio = novo_item
        self.tamanho += 1

    def adicionar_fim(self, valor):
        novo_item = Item(valor)
        if self.is_empty():
            self.inicio = novo_item
            self.fim = novo_item
        else:
            novo_item.ant = self.fim
            self.fim.prox = novo_item
            self.fim = novo_item
        self.tamanho += 1
        
    def remover_inicio(self):
        if self.is_empty():
            raise Exception('A lista está vazia.')
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.prox
            self.inicio.ant = None
        self.tamanho -= 1
          
    def remover_fim(self):
        if self.is_empty():
            raise Exception('A lista está vazia.')
        elif self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.fim = self.fim.ant
            self.fim.prox = None
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