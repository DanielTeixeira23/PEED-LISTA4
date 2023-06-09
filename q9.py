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

    def remover(self, elemento):
        if self.is_empty():
            raise Exception('A lista está vazia.')
        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.valor[0] == elemento:
                if anterior is None:
                    self.inicio = atual.prox
                else:
                    anterior.prox = atual.prox
                self.tamanho -= 1
                return True, atual.valor
            anterior = atual
            atual = atual.prox
        return False, None

    def buscar(self, elemento):
        if self.is_empty():
            raise Exception('A lista está vazia.')
        atual = self.inicio

        while atual is not None:
            if atual.valor[0] == elemento:
                return True, atual.valor
            atual = atual.prox
        return False, None

    def listar(self):
        if self.inicio is None:
            raise Exception('A lista está vazia.')
        atual = self.inicio
        while atual is not None:
            print('{:<15}{:<15}{:<15}'.format(atual.valor[0], atual.valor[1], atual.valor[2]))
            atual = atual.prox

    def obter_tamanho(self):
        return self.tamanho
    
def menu():
    l = ListaEncadeadaSimples()

    while True:
        print('\tMenu')
        print('  1 - Inserir')
        print('  2 - Remover')
        print('  3 - Pesquisar')
        print('\n')
        op = int(input('Digite uma opção: '))

        if op == 1:
            qnt = int(input('Quantos clientes vão ser adicionados: '))
            for i in range(qnt):
                nome = input('Nome do Cliente: ')
                num = int(input('Número da Conta: '))
                saldo = float(input('Saldo: '))
                print()
                l.adicionar_fim((nome, num, saldo))
            print()
            print('Cliente\t\tConta\t\tSaldo')
            print('------------------------------------')
            l.listar()
            print('------------------------------------')
        elif op == 2:
            nome_pesquisar = input('Digite o nome do cliente a ser excluído: ')
            encontrado, cliente = l.remover(nome_pesquisar)
            if encontrado:
                print('Cadastro do cliente removido com sucesso.')
            else:
                print('Cliente não encontrado.')
            print()
            print('Cliente\t\tConta\t\tSaldo')
            print('------------------------------------')
            l.listar()
            print('------------------------------------')
            print()
        elif op == 3:
            nome_pesquisar = input('Digite o nome do cliente a ser pesquisado: ')
            encontrado, cliente = l.buscar(nome_pesquisar)
            if encontrado:
                print('Nome:', cliente[0])
                print('Número da Conta:', cliente[1])
                print('Saldo:', cliente[2])
                print()
            else:
                print('Cliente não encontrado.')
                print()
        else:
            print('Opção inválida. Por favor, digite uma opção válida.')
            
menu()