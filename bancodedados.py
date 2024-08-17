import sqlite3
from sqlite3 import Error

class BancoDeDados:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
        """Inicializa a conexão com o banco de dados"""
        try:
            self.conexao = sqlite3.connect(nome_banco)
            self.cursor = self.conexao.cursor()
            print("Conexão bem-sucedida com o banco de dados!")
        except Error as e:
            print(f"Erro ao conectar com o banco de dados: {e}")

    def criar_tabela(self, create_table_sql):
        """Cria uma tabela com base no comando SQL fornecido"""
        try:
            self.cursor.execute(create_table_sql)
            self.conexao.commit()
            print("Tabela criada com sucesso!")
        except Error as e:
            print(f"Erro ao criar a tabela: {e}")

    def inserir_dados(self, table, data):
        """Insere dados em uma tabela"""
        keys = ', '.join(data.keys())
        question_marks = ', '.join(list('?' * len(data)))
        values = tuple(data.values())
        query = f'INSERT INTO {table} ({keys}) VALUES ({question_marks})'

        try:
            self.cursor.execute(query, values)
            self.conexao.commit()
            print("Dados inseridos com sucesso!")
        except Error as e:
            print(f"Erro ao inserir dados: {e}")

    def buscar_dados(self, table, conditions=None):
        """Busca dados em uma tabela com base nas condições fornecidas"""
        query = f'SELECT * FROM {table}'
        if conditions:
            query += f' WHERE {" AND ".join(conditions)}'
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None

    def atualizar_dados(self, table, updates, conditions):
        """Atualiza dados em uma tabela com base nas condições fornecidas"""
        query = f'UPDATE {table} SET {", ".join(updates)} WHERE {" AND ".join(conditions)}'
        
        try:
            self.cursor.execute(query)
            self.conexao.commit()
            print("Dados atualizados com sucesso!")
        except Error as e:
            print(f"Erro ao atualizar dados: {e}")

    def deletar_dados(self, table, conditions):
        """Deleta dados em uma tabela com base nas condições fornecidas"""
        query = f'DELETE FROM {table} WHERE {" AND ".join(conditions)}'

        try:
            self.cursor.execute(query)
            self.conexao.commit()
            print("Dados deletados com sucesso!")
        except Error as e:
            print(f"Erro ao deletar dados: {e}")

    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados"""
        if self.cursor:
            self.cursor.close()
            print("Conexão com o banco de dados fechada!")
            
    def criar_tabelas_completas(self):
        """Cria todas as tabelas necessárias no banco de dados"""
        comando = ''
        t= open('tabelas.sql','r')
        for l in t.readlines():
            if '--' not in l:
                comando += l
            if ';' in l:
                self.criar_tabela(comando)
                print(comando)
                comando = ''
        t.close()
    
    def executar_comando(self, sql, parametros=(), retorna_resultado=False):
        try:
            self.cursor.execute(sql, parametros)
            if retorna_resultado:
                return self.cursor.fetchall()
            self.conexao.commit()
        except sqlite3.Error as e:
            print(f"Erro ao executar comando: {e}")
        finally:
            self.cursor.close()
            self.conexao.close()
    
    def consultar(self, sql, parametros=None):
        if parametros:
            self.cursor.execute(sql, parametros)
        else:
            self.cursor.execute(sql)
        return self.cursor.fetchall()
        
    def criar_pessoa(self, nome, data_nascimento, cpf, genero, email):
        sql = """
        INSERT INTO Pessoa (nome, data_nascimento, cpf, genero, email)
        VALUES (?, ?, ?, ?, ?)
        """
        parametros = (nome, data_nascimento, cpf, genero, email)
        self.executar_comando(sql, parametros)

    def ler_pessoa(self, sql, parametros=()):
        try:
            self.cursor.execute(sql, parametros)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao ler dados: {e}")
        finally:
            self.cursor.close()
            self.conexao.close()

    def atualizar_pessoa(self, id_pessoa, nome=None, data_nascimento=None, cpf=None, genero=None, email=None):
        campos = []
        valores = []
        if nome:
            campos.append("nome = ?")
            valores.append(nome)
        if data_nascimento:
            campos.append("data_nascimento = ?")
            valores.append(data_nascimento)
        if cpf:
            campos.append("cpf = ?")
            valores.append(cpf)
        if genero:
            campos.append("genero = ?")
            valores.append(genero)
        if email:
            campos.append("email = ?")
            valores.append(email)
        valores.append(id_pessoa)
        sql = f"UPDATE Pessoa SET {', '.join(campos)} WHERE id_pessoa = ?"
        self.executar_comando(sql, valores)

    def deletar_pessoa(self, id_pessoa):
        sql = "DELETE FROM Pessoa WHERE id_pessoa = ?"
        self.executar_comando(sql, (id_pessoa,))
    
    def criar_produto(self, id_vendedor, nome, descricao, categoria, preco, quantidade_estoque, data_cadastro):
        sql = """
        INSERT INTO Produto (id_vendedor, nome, descricao, categoria, preco, quantidade_estoque, data_cadastro)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        parametros = (id_vendedor, nome, descricao, categoria, preco, quantidade_estoque, data_cadastro)
        self.executar_comando(sql, parametros)

    def ler_produto(self, id_produto):
        sql = "SELECT * FROM Produto WHERE id_produto = ?"
        return self.consultar(sql, (id_produto,))

    def atualizar_produto(self, id_produto, nome=None, descricao=None, categoria=None, preco=None, quantidade_estoque=None):
        campos = []
        valores = []
        if nome:
            campos.append("nome = ?")
            valores.append(nome)
        if descricao:
            campos.append("descricao = ?")
            valores.append(descricao)
        if categoria:
            campos.append("categoria = ?")
            valores.append(categoria)
        if preco:
            campos.append("preco = ?")
            valores.append(preco)
        if quantidade_estoque:
            campos.append("quantidade_estoque = ?")
            valores.append(quantidade_estoque)
        valores.append(id_produto)
        sql = f"UPDATE Produto SET {', '.join(campos)} WHERE id_produto = ?"
        self.executar_comando(sql, valores)

    def deletar_produto(self, id_produto):
        sql = "DELETE FROM Produto WHERE id_produto = ?"
        self.executar_comando(sql, (id_produto,))
    
        
if __name__ == "__main__":
    database = BancoDeDados("cadastro_unico.db")
    database.criar_tabelas_completas()
       
    # Criar uma nova pessoa
    database.criar_pessoa("Maria Silva", "1990-01-01", "123.456.789-00", "Feminino", "maria@example.com")

    # Ler os dados da pessoa
    pessoa = database.ler_pessoa(1)
    print(pessoa)

    # Atualizar dados da pessoa
    database.atualizar_pessoa(1, nome="Maria de Souza Silva")

    # Deletar a pessoa
    database.deletar_pessoa(1)

    database.fechar_conexao()

