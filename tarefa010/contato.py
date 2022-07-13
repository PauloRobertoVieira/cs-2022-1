'''Exercício 01: Crie uma classe com o nome _Contato_ que possui dois atributos: nome e email do tipo String.
Crie outra classe, chamada Agenda, que possui um atributo contatos do tipo List<Contato>.
A classe Agenda deve conter um método para adicionar um novo contato,
um método para buscar um contato pelo seu nome ou email (retorna uma instância de Contato),
um método para excluir um contato através do nome e por fim
um método para listar os contatos adicionados na agenda.'''


class Contato:
    def __init__(self, nome, email=None):
        self.nome = nome
        self.email = email

    def __str__(self):
        return self.nome


class Agenda():
    contatos = []

    def __str__(self):
        nomes = ''
        for contato in self.contatos:
            nomes += f'{contato.nome}\n'
        return nomes

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def buscar(self, nome):
        for apelido in self.contatos:
            if apelido.nome == nome:
                return apelido

    def excluir_contato(self, nome):
        for apelido in self.contatos:
            if apelido.nome == nome:
                self.contatos.remove(apelido)

    def listar_contato(self):
        resultado = ''
        for contato in self.contatos:
            resultado += f'{contato.nome}\n'
        return resultado


agenda = Agenda()
contato1 = Contato('Ana', 'anamaria@gmail.com')
agenda.adicionar_contato(contato1)

contato2 = Contato('Ze', 'ze@gmail.com')
agenda.adicionar_contato(contato2)

contato3 = Contato('xyz', 'xyz@gmail.com')
agenda.adicionar_contato(contato3)

contato4 = Contato('Pedro', 'Pedro@gmail.com')
agenda.adicionar_contato(contato4)

print('Nome encontrado: ', agenda.buscar('Ana'))

print('\nLista contatos:')
print(agenda.listar_contato())

agenda.excluir_contato('xyz')
print('\nRemovido:')
print(agenda.listar_contato())
