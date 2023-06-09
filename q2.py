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
            raise Exception('A lista está vazia')
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return valor
    
    def listar(self):
        if self.inicio is None:
            raise Exception('A lista está vazia.')
        atual = self.inicio
        while atual is not None:
            print(atual.valor, end=' ')
            atual = atual.proximo
    
    def obter_tamanho(self):
        return self.tamanho

def menu():
    f = Fila()
    
    while True:
        print('\tMenu')
        print('  1 - Adicionar')
        print('  2 - Remover')
        print('  3 - Tamanho da Fila')
        print('  4 - Mostrar Fila')
        print('  5 - Sair')
        print('\n')
        op = int(input('Digite uma opção: '))
        
        if op == 1:
            qnt = int(input('Quantos números serão adicionados: '))
            for i in range(qnt):
                num = int(input(f'Digite o {i+1}° número: '))
                f.adicionar(num)
            print('Números adicionados com sucesso.')
        elif op == 2:
            num_remover = f.remover()
            print(f'Numero {num_remover} removido com sucesso.')
        elif op == 3:
            print('Tamanho da fila: ', f.obter_tamanho())
        elif op == 4:
            f.listar()
            print('\n')
        elif op == 5:
            print('Saindo...')
            break  
        else:
            print('Opção inválida. Tente novamente.')    
    return f  

ordem = menu()       