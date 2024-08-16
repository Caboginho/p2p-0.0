from bancodedados import BancoDeDados
class AgendaDAO(BancoDeDados):
    def __init__(self, nome_banco):
        super().__init__(nome_banco)

    def criar(self, id_servico, data_horario, status):
        comando = """
        INSERT INTO Agenda (id_servico, data_horario, status) 
        VALUES (?, ?, ?);
        """
        self.executar_comando(comando, (id_servico, data_horario, status))

    def ler(self, id_agenda):
        comando = "SELECT * FROM Agenda WHERE id_agenda = ?;"
        return self.consultar(comando, (id_agenda,))

    def atualizar(self, id_agenda, id_servico, data_horario, status):
        comando = """
        UPDATE Agenda
        SET id_servico = ?, data_horario = ?, status = ?
        WHERE id_agenda = ?;
        """
        self.executar_comando(comando, (id_servico, data_horario, status, id_agenda))

    def deletar(self, id_agenda):
        comando = "DELETE FROM Agenda WHERE id_agenda = ?;"
        self.executar_comando(comando, (id_agenda,))
