import sqlite3


conn = sqlite3.connect('db_concessionaria.db')
cursor = conn.cursor()

cursor.execute(
"""
CREATE TABLE veiculos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50),
    marca VARCHAR(20),
    modelo VARCHAR(20),
    cor VARCHAR(20),
    placa VARCHAR(7),
    proprietario VARCHAR(50),
    num_portas INT,
    km_rodado INT,
    qtd_passageiros INT,
    ano INTEGER,
    valor INTEGER,
    motor INT,
    combustivel VARCHAR(20),
    meio_locomocao VARCHAR(30) 
);               
""")

cursor.execute(
"""
CREATE TABLE pessoas(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    veiculo_id INTEGER,

    FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)   
        
);
""")
print('Tabela criada com sucesso.')

conn.close()

class Pessoa:

    def __init__(self, nome, data_nascimento, cpf, endereco, salario, profissao, email,
                telefone, nome_do_responsavel, sexo, naturalidade, nacionalidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.salario = salario
        self.profissao = profissao
        self.email = email
        self.telefone = telefone
        self.nome_do_responsavel = nome_do_responsavel
        self.sexo = sexo
        self.naturalidade = naturalidade
        self.nacionalidade = nacionalidade


    
