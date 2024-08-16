from bancodedados import BancoDeDados
from Pessoa import Pessoa
# A classe PessoaJuridicatambém herdada da classe Pessoae 
# inclui atributos como CNPJ, nome fantasia e razão social.
class PessoaJuridica(Pessoa):
    def __init__(self, nome_fantasia, razao_social, cnpj, email, telefone=None, endereco=None):
        super().__init__(nome_fantasia, email, telefone, endereco)
        self.razao_social = razao_social
        self.cnpj = cnpj

    def salvar(self):
        comando = """
        INSERT INTO PessoaJuridica (nome_fantasia, razao_social, cnpj, email, telefone, endereco) 
        VALUES (?, ?, ?, ?, ?, ?);
        """
        BancoDeDados().executar_comando(comando, (self.nome, self.razao_social, self.cnpj, self.email, self.telefone, self.endereco))

    def atualizar(self, id_pessoa_juridica):
        comando = """
        UPDATE PessoaJuridica
        SET nome_fantasia = ?, razao_social = ?, cnpj = ?, email = ?, telefone = ?, endereco = ?
        WHERE id_pessoa_juridica = ?;
        """
        BancoDeDados().executar_comando(comando, (self.nome, self.razao_social, self.cnpj, self.email, self.telefone, self.endereco, id_pessoa_juridica))

    def deletar(self, id_pessoa_juridica):
        comando = "DELETE FROM PessoaJuridica WHERE id_pessoa_juridica = ?;"
        BancoDeDados().executar_comando(comando, (id_pessoa_juridica,))

    def buscar(self, id_pessoa_juridica):
        comando = "SELECT * FROM PessoaJuridica WHERE id_pessoa_juridica = ?;"
        return BancoDeDados().consultar(comando, (id_pessoa_juridica,))
