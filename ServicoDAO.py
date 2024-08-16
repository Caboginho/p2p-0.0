from bancodedados import BancoDeDados
class ServicoDAO(BancoDeDados):
    def __init__(self, nome_banco):
        super().__init__(nome_banco)

    def criar(self, id_prestador, nome, descricao, id_tipo_servico, preco, data_inicio, data_fim, disponibilidade):
        comando = """
        INSERT INTO Servico (id_prestador, nome, descricao, id_tipo_servico, preco, data_inicio, data_fim, disponibilidade) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """
        self.executar_comando(comando, (id_prestador, nome, descricao, id_tipo_servico, preco, data_inicio, data_fim, disponibilidade))

    def ler(self, id_servico):
        comando = "SELECT * FROM Servico WHERE id_servico = ?;"
        return self.consultar(comando, (id_servico,))

    def atualizar(self, id_servico, nome, descricao, id_tipo_servico, preco, data_inicio, data_fim, disponibilidade):
        comando = """
        UPDATE Servico
        SET nome = ?, descricao = ?, id_tipo_servico = ?, preco = ?, data_inicio = ?, data_fim = ?, disponibilidade = ?
        WHERE id_servico = ?;
        """
        self.executar_comando(comando, (nome, descricao, id_tipo_servico, preco, data_inicio, data_fim, disponibilidade, id_servico))

    def deletar(self, id_servico):
        comando = "DELETE FROM Servico WHERE id_servico = ?;"
        self.executar_comando(comando, (id_servico,))
