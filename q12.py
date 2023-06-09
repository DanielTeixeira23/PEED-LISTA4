class Item:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
        self.ant = None
        self.dado = valor

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

    def remover_inicio(self, nome):
        if self.is_empty():
            raise Exception('A lista está vazia.')

        atual = self.fim
        while atual is not None:
            if atual.dado[0] == nome:
                if self.inicio == self.fim:
                    self.inicio = None
                    self.fim = None
                else:
                    if atual == self.fim:
                        self.fim = atual.ant
                        self.fim.prox = None
                    elif atual == self.inicio:
                        self.inicio = atual.prox
                        self.inicio.ant = None
                    else:
                        atual.ant.prox = atual.prox
                        atual.prox.ant = atual.ant
                self.tamanho -= 1
                return
            atual = atual.ant
        raise Exception('O contato informado não foi encontrado.')
    
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
            if atual.dado[0] == elemento:
                return atual.dado[1]
            atual = atual.prox
        return False

    def listar(self):
        if self.inicio is None:
            raise Exception('A lista está vazia.')
        atual = self.inicio
        while atual is not None:
            nome, num = atual.dado
            print(f'{nome:<10} {num:<11}')
            atual = atual.prox
            
    def obter_tamanho(self):
        return self.tamanho


def agenda():
    l = ListaEncadeadaDupla()
    
    while True:
        print('\t  Agenda Telefônica')
        print('\t1 - Adicionar')
        print('\t2 - Remover')
        print('\t3 - Buscar')
        print('\t4 - Contatos')
        print('\t0 - Sair')
        print()
        op = int(input('Digite a opção desejada: '))

        if op == 1:
            qnt = int(input('Quantos números serão adicionados: '))
            for i in range(qnt):
                nome = input(f'Digite o nome da {i+1}ª pessoa: ')
                num = input('Número: ')
                l.adicionar_fim((nome, num))
            print('Números adicionados com sucesso.')
        elif op == 2:
            nome = input('Digite o nome para ser removido: ')
            excluir = l.buscar(nome)
            if excluir:
                l.remover_inicio(nome)
                print('Contato removido com sucesso.')
            else:
                print('O contato informado não foi encontrado.')
        elif op == 3:
            nome = input('Digite o nome a ser buscado: ')
            encontrado = l.buscar(nome)
            if encontrado:
                num = encontrado
                print('Nome: ',nome,'Telefone: ', num)
            else:
                print('Contato não encontrado.')
        elif op == 4:
            print('Lista de Contatos')
            print('Nome\tNúmero')
            l.listar()
        elif op == 0:
            print('Saindo...')
            break
        else:
            print('Opção inválida.')

agenda()