from bancodedados import BancoDeDados
from Pessoa import Pessoa
# A classe PessoaJuridicatambém herdada da classe Pessoae 
# inclui atributos como CNPJ, nome fantasia e razão social.
class PessoaJuridica(Pessoa):
    def __init__(self, nome_fantasia, razao_social, cnpj, email, telefone=None, endereco=None):
        super().__init__(nome_fantasia, email, telefone, endereco)
        self.nome_fantasia = nome_fantasia
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.nome_banco = 'cadastro_unico.db'

    def salvar(self):
        banco = BancoDeDados(self.nome_banco)
        if self.existe_cnpj(banco):
            print("CNPJ já cadastrado. Atualizando o registro existente.")
            self.atualizar(banco)
        else:
            comando = '''
            INSERT INTO PessoaJuridica (nome_fantasia, razao_social, cnpj, email, telefone, endereco)
            VALUES (?, ?, ?, ?, ?, ?)
            '''
            banco.executar_comando(comando, (self.nome_fantasia, self.razao_social, self.cnpj, self.email, self.telefone, self.endereco))
            print("Pessoa Jurídica criada com sucesso!")

    def existe_cnpj(self, banco):
        comando = '''
        SELECT COUNT(*) FROM PessoaJuridica WHERE cnpj = ?
        '''
        resultado = BancoDeDados(self.nome_banco).executar_comando(comando, (self.cnpj,), retorna_resultado=True)
        return resultado[0][0] > 0
    
    def buscar(self, id):
        comando = '''
        SELECT * FROM PessoaJuridica WHERE id = ?
        '''
        banco = BancoDeDados(self.nome_banco)
        resultado = banco.ler_pessoa(comando, (id,))
        return resultado
    
    def atualizar(self, banco):
        comando = '''
        UPDATE PessoaJuridica
        SET nome_fantasia = ?, razao_social = ?, email = ?, telefone = ?, endereco = ?
        WHERE cnpj = ?
        '''
        BancoDeDados(self.nome_banco).executar_comando(comando, (self.nome_fantasia, self.razao_social, self.email, self.telefone, self.endereco, self.cnpj))
        print("Pessoa Jurídica atualizada com sucesso!")
        
    def deletar(self, id):
        comando = "DELETE FROM PessoaJuridica WHERE id = ?"
        BancoDeDados(self.nome_banco).executar_comando(comando, (id,))