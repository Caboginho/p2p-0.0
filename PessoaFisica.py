from bancodedados import BancoDeDados
from Pessoa import Pessoa
# A classe PessoaFisicaherdada da classe Pessoae adiciona 
# atributos específicos, CPF e dados de nascimento.
class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, email, telefone=None, endereco=None):
        super().__init__(nome, email, telefone, endereco)
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.nome_banco = 'cadastro_unico.db'

    def salvar(self):
        comando = """INSERT INTO PessoaFisica (nome, cpf, data_nascimento, email, telefone, endereco)
                     VALUES (?, ?, ?, ?, ?, ?)"""
        BancoDeDados(self.nome_banco).executar_comando(comando, (self.nome, self.cpf, self.data_nascimento, self.email, self.telefone, self.endereco))

    def buscar(self, id):
        comando = "SELECT * FROM PessoaFisica WHERE id = ?"
        return BancoDeDados(self.nome_banco).consultar(comando, (id,))

    def atualizar(self, id):
        comando = """UPDATE PessoaFisica SET nome = ?, cpf = ?, data_nascimento = ?, email = ?, telefone = ?, endereco = ?
                     WHERE id = ?"""
        BancoDeDados(self.nome_banco).executar_comando(comando, (self.nome, self.cpf, self.data_nascimento, self.email, self.telefone, self.endereco, id))

    def deletar(self, id):
        comando = "DELETE FROM PessoaFisica WHERE id = ?"
        BancoDeDados(self.nome_banco).executar_comando(comando, (id,))

