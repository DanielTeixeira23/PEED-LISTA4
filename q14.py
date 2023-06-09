class Item:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeadaCircular:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def is_empty(self):
        return self.inicio is None
    
    def obter_tamanho(self):
        return self.tamanho
    
    def inserir_inicio(self, valor):
        novo_item = Item(valor)
        novo_item.proximo = self.inicio
        self.inicio = novo_item
        self.tamanho +=1
        if self.tamanho == 1:
            self.fim = self.inicio
            self.fim.proximo = self.inicio
    
    def inserir_final(self, valor):
        novo_item = Item(valor)
        if self.inicio is None:
            self.inicio = novo_item
        else:
            atual = self.inicio
            while atual != self.fim:
                atual = atual.proximo
            atual.proximo = novo_item
        self.fim = novo_item
        self.fim.proximo = self.inicio
        self.tamanho += 1
        
    def remover_inicio(self):
        if self.inicio is None:
            raise Exception('A lista está vazia!')
        else:
            self.inicio = self.inicio.proximo
        self.tamanho -=1
        
    def remover_final(self):
        if self.is_empty():
            raise Exception('A lista está vazia!')
        
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        
        atual = self.inicio
        anterior = None
        while atual != self.fim:
            anterior = atual
            atual = atual.proximo
        anterior.proximo = self.inicio
        self.fim = anterior
        self.tamanho -=1
        
    def listar(self):
        if self.is_empty():
            raise Exception("A lista está vazia!")
        atual = self.inicio
        
        while atual != self.fim:
            print(atual.dado, end= '\n')
            atual = atual.proximo
        print(atual.dado)
        
    def buscar(self, valor):
        if self.inicio is None:
            raise Exception('A lista está vazia!')
        atual = self.inicio
        while atual != self.fim:
            if atual.dado == valor:
                return True
            atual = atual.proximo
        return False 
        
    def primeiro(self):
        if self.is_empty():
            raise Exception("A lista está vazia!")
        return self.inicio.dado
    
    def ultimo(self):
        if self.is_empty():
            raise Exception("A lista está vazia!")
        return self.fim.dado

def lista():
    l = ListaEncadeadaCircular()
    numeros = []
    
    qnt = int(input('Quantos número vão ser adicionados: '))
    for i in range(qnt):
        num = int(input(f'Digite o {i+1}º número: '))
        numeros.append(num)
        
    ordem_crecente = sorted(numeros, reverse=False)
    
    for num in ordem_crecente:
        l.inserir_final(num)
    
    l.listar()
    print('Primeiro elemento da lista: ', l.primeiro())
    print('Último elemento da lista: ', l.ultimo())
    
lista()