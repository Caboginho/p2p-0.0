from bancodedados import BancoDeDados
class TransacaoDAO(BancoDeDados):
    def __init__(self, nome_banco):
        super().__init__(nome_banco)

    def criar(self, id_comprador, id_vendedor, id_produto, id_servico, data_transacao, valor):
        comando = """
        INSERT INTO Transacao (id_comprador, id_vendedor, id_produto, id_servico, data_transacao, valor) 
        VALUES (?, ?, ?, ?, ?, ?);
        """
        self.executar_comando(comando, (id_comprador, id_vendedor, id_produto, id_servico, data_transacao, valor))

    def ler(self, id_transacao):
        comando = "SELECT * FROM Transacao WHERE id_transacao = ?;"
        return self.consultar(comando, (id_transacao,))

    def atualizar(self, id_transacao, id_comprador, id_vendedor, id_produto, id_servico, data_transacao, valor):
        comando = """
        UPDATE Transacao
        SET id_comprador = ?, id_vendedor = ?, id_produto = ?, id_servico = ?, data_transacao = ?, valor = ?
        WHERE id_transacao = ?;
        """
        self.executar_comando(comando, (id_comprador, id_vendedor, id_produto, id_servico, data_transacao, valor, id_transacao))

    def deletar(self, id_transacao):
        comando = "DELETE FROM Transacao WHERE id_transacao = ?;"
        self.executar_comando(comando, (id_transacao,))
