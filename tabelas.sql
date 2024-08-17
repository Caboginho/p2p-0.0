--Estrutura Completa do Banco de Dados
--Tabela Pessoa
--Tabela central com os dados básicos do cidadão.
CREATE TABLE Pessoa (
    id_pessoa INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    rg VARCHAR(15) UNIQUE,
    genero VARCHAR(100),
    nacionalidade VARCHAR(100),
    estado_civil VARCHAR(100),
    email VARCHAR(100),
    endereco_id INT,
    FOREIGN KEY (endereco_id) REFERENCES Endereco(id_endereco)
);
--Tabela Endereco
--Tabela para armazenar os endereços.
CREATE TABLE Endereco (
    id_endereco INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pessoa INT,
    logradouro VARCHAR(255),
    numero VARCHAR(10),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    estado VARCHAR(100),
    cep VARCHAR(10),
    pais VARCHAR(100),
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa)
);
--Tabela Documento
--Tabela para documentos como RG, CPF, CNH, etc.
CREATE TABLE IF NOT EXISTS Documento (
    id_documento INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pessoa INTEGER,
    id_tipo_documento INTEGER NOT NULL,
    numero_documento TEXT UNIQUE NOT NULL,
    data_emissao TEXT,
    data_validade TEXT,
    orgao_emissor TEXT,
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa),
    FOREIGN KEY (id_tipo_documento) REFERENCES TipoDocumento(id_tipo_documento)
);
--Tabela Saude
--Tabela para armazenar informações relacionadas à saúde.
CREATE TABLE Saude (
    id_saude INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pessoa INT,
    tipo_informacao VARCHAR(255),
    descricao TEXT,
    data_registro DATE,
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa)
);
--Tabela Educacao
--Tabela para informações educacionais.
CREATE TABLE Educacao (
    id_educacao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pessoa INT,
    instituicao VARCHAR(255),
    curso VARCHAR(255),
    nivel VARCHAR(255),
    data_inicio DATE,
    data_conclusao DATE,
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa)
);
--Tabela Trabalho
--Tabela para registrar a trajetória profissional
CREATE TABLE Trabalho (
    id_trabalho INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pessoa INT,
    empresa VARCHAR(255),
    cargo VARCHAR(255),
    data_admissao DATE,
    data_demissao DATE,
    descricao_atividades TEXT,
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa)
);
--Tabela Justica
--Tabela para informações relacionadas a processos judiciais.
CREATE TABLE Justica (
    id_justica INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pessoa INT,
    tipo_processo VARCHAR(255),
    numero_processo VARCHAR(50),
    descricao TEXT,
    data_inicio DATE,
    data_fim DATE,
    resultado VARCHAR(255),
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa)
);
--Tabela Negocio
--Para registros de empreendimentos, empresas e negócios.
CREATE TABLE Negocio (
    id_negocio INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pessoa INT,
    nome_empresa VARCHAR(255),
    cnpj VARCHAR(14) UNIQUE,
    data_abertura DATE,
    data_fechamento DATE,
    descricao_atividade TEXT,
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa)
);
--Tabela SegurancaSocial
--Informações sobre benefícios e aposentadorias.
CREATE TABLE SegurancaSocial (
    id_seg_social INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pessoa INT,
    tipo_beneficio VARCHAR(255),
    data_inicio DATE,
    data_fim DATE,
    valor_mensal DECIMAL(10, 2),
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa)
);
--Tabela TransacaoP2P
--Registros de transações realizadas na rede P2P.
CREATE TABLE TransacaoP2P (
    id_transacao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pessoa INT,
    tipo_transacao VARCHAR(255),
    descricao TEXT,
    valor DECIMAL(10, 2),
    data_transacao DATE,
    FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa)
);
--Tabela Produto
--Esta tabela armazenará informações sobre os produtos disponíveis.
CREATE TABLE IF NOT EXISTS Produto (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    id_vendedor INTEGER,
    nome TEXT NOT NULL,
    descricao TEXT,
    categoria TEXT,
    preco REAL NOT NULL,
    quantidade_estoque INTEGER NOT NULL,
    data_cadastro TEXT,
    FOREIGN KEY (id_vendedor) REFERENCES Pessoa(id_pessoa)
);
--Tabela Servico
CREATE TABLE IF NOT EXISTS Servico (
    id_servico INTEGER PRIMARY KEY AUTOINCREMENT,
    id_prestador INTEGER,
    nome TEXT NOT NULL,
    descricao TEXT,
    id_tipo_servico INTEGER,
    preco REAL,
    data_inicio TEXT,
    data_fim TEXT,
    disponibilidade TEXT,
    FOREIGN KEY (id_prestador) REFERENCES Pessoa(id_pessoa),
    FOREIGN KEY (id_tipo_servico) REFERENCES TipoServico(id_tipo_servico)
);
--Tabela "Agendar Serviço
CREATE TABLE IF NOT EXISTS AgendaServico (
    id_agenda INTEGER PRIMARY KEY AUTOINCREMENT,
    id_servico INTEGER,
    id_cliente INTEGER,
    data_agendamento TEXT NOT NULL,
    hora_inicio TEXT NOT NULL,
    hora_fim TEXT NOT NULL,
    id_status_agenda INTEGER NOT NULL,
    FOREIGN KEY (id_servico) REFERENCES Servico(id_servico),
    FOREIGN KEY (id_cliente) REFERENCES Pessoa(id_pessoa),
    FOREIGN KEY (id_status_agenda) REFERENCES StatusAgenda(id_status_agenda)
);

--Tabela de Tipos de Documentos
CREATE TABLE IF NOT EXISTS TipoDocumento (
    id_tipo_documento INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT UNIQUE NOT NULL
);
--Tabela de Tipos de Serviço
CREATE TABLE IF NOT EXISTS TipoServico (
    id_tipo_servico INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT UNIQUE NOT NULL
);
--Tabela de Status de Agendamento
CREATE TABLE IF NOT EXISTS StatusAgenda (
    id_status_agenda INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT UNIQUE NOT NULL
);
--Tabela da Pessoa Juridica 
CREATE TABLE PessoaJuridica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_fantasia TEXT NOT NULL,
    razao_social TEXT NOT NULL,
    cnpj TEXT UNIQUE NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT,
    endereco TEXT
);
--Tabela da Pessoa fisica 
CREATE TABLE IF NOT EXISTS PessoaFisica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL,
    data_nascimento TEXT NOT NULL,
    email TEXT,
    telefone TEXT,
    endereco TEXT
);
--Campos:
--id_produto: Identificador único do produto.
--id_vendedor: Referência ao vendedor (Pessoa que oferece o produto).
--nome: Nome do produto.
--descricao: Descrição detalhada do produto.
--categoria: Categoria do produto (ex: Eletrônicos, Roupas, etc.).
--preco: Preço do produto.
--quantidade_estoque: Quantidade disponível em estoque.
--data_cadastro: Data em que o produto foi cadastrado.
