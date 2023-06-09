import time
import random

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
    
def fila_supermercado():
    l = Fila()
    lista = []
    
    qnt = int(input('Quantidade de Clientes: '))
    
    for i in range(qnt):
        cliente = int(input(f'Cliente: '))
        numero_ind = random.randint(0, 100)
        l.adicionar(cliente)
        lista.append(numero_ind)
        
    print()
    print('Atendimento iniciado.')
    while not l.is_empty():
        if not l.is_empty():
            print('Cliente: ', l.remover())
            print('Número identifacação: ', lista.pop())
            time.sleep(5)
            print('Cliente antendido.')
            print()
        if l.is_empty():
            print('Atendimento encerrado.') 
            
    return l
        
fila_supermercado()