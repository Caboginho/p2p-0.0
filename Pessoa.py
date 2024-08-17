from abc import ABC, abstractmethod
# Uma classe Pessoaserá uma classe abstrata que define os atributos 
# e métodos comuns para PessoaFisicae PessoaJuridica.
class Pessoa(ABC):
    def __init__(self, nome, email, telefone=None, endereco=None):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        
    @abstractmethod
    def salvar(self):
        pass

    @abstractmethod
    def atualizar(self):
        pass

    @abstractmethod
    def deletar(self):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

