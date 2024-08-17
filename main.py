from bancodedados import BancoDeDados
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

def main():
    # Definindo o nome do banco de dados
    nome_banco = "cadastro_unico.db"
    
    # Instanciando o banco de dados e criando tabelas
    banco = BancoDeDados(nome_banco)
    banco.criar_tabelas_completas()

    # Criando e testando operações com PessoaFisica e PessoaJuridica
    print("** Criando Pessoa Física **")
    pessoa_fisica = PessoaFisica(nome="João Silva", cpf="12345678901", data_nascimento="1985-05-15", email="joao.silva@example.com", telefone="123456789", endereco="Rua A, 123")
    pessoa_fisica.salvar()
    print("Pessoa Física criada com sucesso!")

    # Lendo dados da Pessoa Física
    print("\n** Lendo Pessoa Física **")
    pessoa_fisica_lida = pessoa_fisica.buscar(1)
    print(f"Dados da Pessoa Física: {pessoa_fisica_lida}")

    # Atualizando dados da Pessoa Física
    print("\n** Atualizando Pessoa Física **")
    pessoa_fisica.nome = "João Carlos Silva"
    pessoa_fisica.atualizar(1)
    print("Pessoa Física atualizada com sucesso!")

    # Lendo dados atualizados da Pessoa Física
    print("\n** Lendo Pessoa Física Atualizada **")
    pessoa_fisica_lida = pessoa_fisica.buscar(1)
    print(f"Dados atualizados da Pessoa Física: {pessoa_fisica_lida}")

    # Criando Pessoa Jurídica
    print("\n** Criando Pessoa Jurídica **")
    pessoa_juridica = PessoaJuridica(nome_fantasia="Empresa XYZ", razao_social="Empresa XYZ LTDA", cnpj="98765432100123", email="contato@xyz.com", telefone="987654321", endereco="Avenida B, 456")
    pessoa_juridica.salvar()
    print("Pessoa Jurídica criada com sucesso!")

    # Lendo dados da Pessoa Jurídica
    print("\n** Lendo Pessoa Jurídica **")
    pessoa_juridica_lida = pessoa_juridica.buscar(1)
    print(f"Dados da Pessoa Jurídica: {pessoa_juridica_lida}")

    # Atualizando dados da Pessoa Jurídica
    print("\n** Atualizando Pessoa Jurídica **")
    pessoa_juridica.nome_fantasia = "Empresa ABC"
    pessoa_juridica.atualizar(1)
    print("Pessoa Jurídica atualizada com sucesso!")

    # Lendo dados atualizados da Pessoa Jurídica
    print("\n** Lendo Pessoa Jurídica Atualizada **")
    pessoa_juridica_lida = pessoa_juridica.buscar(1)
    print(f"Dados atualizados da Pessoa Jurídica: {pessoa_juridica_lida}")

    # Deletando Pessoa Física e Jurídica
    print("\n** Deletando Pessoa Física **")
    pessoa_fisica.deletar(1)
    print("Pessoa Física deletada com sucesso!")

    print("\n** Deletando Pessoa Jurídica **")
    pessoa_juridica.deletar(1)
    print("Pessoa Jurídica deletada com sucesso!")

if __name__ == "__main__":
    main()
