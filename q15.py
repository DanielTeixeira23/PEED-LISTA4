import random 

class Item:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaCircular:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def vazia(self):
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
        if self.vazia():
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
        if self.vazia():
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
    
def roleta():
    l = ListaCircular()
    for i in range(10):
        l.inserir_final(i)
        
    num = int(input('De 0 a 10 escolha um número para apostar: '))
    sorteio = random.randint(0, 50)
        
    aux = l.inicio
    giro = sorteio
    x = 0
    while giro > 0:
        s = aux.dado
        aux = aux.proximo
        giro -= 1
        
    if num == s:
        print('O número sorteado foi: ', s)
        print('Você ganhou!')
    else:
        print('O número sorteado foi:', s)
        print('Você perdeu!')
           
roleta()