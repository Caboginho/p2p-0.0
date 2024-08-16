from bancodedados import BancoDeDados
class ProdutoDAO(BancoDeDados):
    def __init__(self, nome_banco):
        super().__init__(nome_banco)

    def criar(self, id_vendedor, nome, descricao, categoria, preco, quantidade_estoque):
        comando = """
        INSERT INTO Produto (id_vendedor, nome, descricao, categoria, preco, quantidade_estoque) 
        VALUES (?, ?, ?, ?, ?, ?);
        """
        self.executar_comando(comando, (id_vendedor, nome, descricao, categoria, preco, quantidade_estoque))

    def ler(self, id_produto):
        comando = "SELECT * FROM Produto WHERE id_produto = ?;"
        return self.consultar(comando, (id_produto,))

    def atualizar(self, id_produto, nome, descricao, categoria, preco, quantidade_estoque):
        comando = """
        UPDATE Produto
        SET nome = ?, descricao = ?, categoria = ?, preco = ?, quantidade_estoque = ?
        WHERE id_produto = ?;
        """
        self.executar_comando(comando, (nome, descricao, categoria, preco, quantidade_estoque, id_produto))

    def deletar(self, id_produto):
        comando = "DELETE FROM Produto WHERE id_produto = ?;"
        self.executar_comando(comando, (id_produto,))
