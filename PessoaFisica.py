from bancodedados import BancoDeDados
from Pessoa import Pessoa
# A classe PessoaFisicaherdada da classe Pessoae adiciona 
# atributos específicos, CPF e dados de nascimento.
class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, email, telefone=None, endereco=None):
        super().__init__(nome, email, telefone, endereco)
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def salvar(self):
        comando = """
        INSERT INTO PessoaFisica (nome, cpf, data_nascimento, email, telefone, endereco) 
        VALUES (?, ?, ?, ?, ?, ?);
        """
        BancoDeDados().executar_comando(comando, (self.nome, self.cpf, self.data_nascimento, self.email, self.telefone, self.endereco))

    def atualizar(self, id_pessoa_fisica):
        comando = """
        UPDATE PessoaFisica
        SET nome = ?, cpf = ?, data_nascimento = ?, email = ?, telefone = ?, endereco = ?
        WHERE id_pessoa_fisica = ?;
        """
        BancoDeDados().executar_comando(comando, (self.nome, self.cpf, self.data_nascimento, self.email, self.telefone, self.endereco, id_pessoa_fisica))

    def deletar(self, id_pessoa_fisica):
        comando = "DELETE FROM PessoaFisica WHERE id_pessoa_fisica = ?;"
        BancoDeDados().executar_comando(comando, (id_pessoa_fisica,))

    def buscar(self, id_pessoa_fisica):
        comando = "SELECT * FROM PessoaFisica WHERE id_pessoa_fisica = ?;"
        return BancoDeDados().consultar(comando, (id_pessoa_fisica,))

