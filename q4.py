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

def palindromo(texto):
    f = Fila()
    
    for i in texto:
        f.adicionar(i)
    
    frase = ''
    while not f.is_empty():
        caracter = f.remover()
        frase = caracter + frase
    return frase == texto

frase_digitada = input('Digite uma frase: ')
resultado = palindromo(frase_digitada)

if resultado:
    print('A frase é um palíndromo.')
else: 
    print("A frase não é um palíndromo.")