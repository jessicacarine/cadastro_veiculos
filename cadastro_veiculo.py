import sqlite3


conn = sqlite3.connect('db_concessionaria.db')
cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE veiculos(
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         nome Varchar(50),
#         marca TEXT NOT NULL,
#         modelo TEXT NOT NULL,
#         cor TEXT,
#         placa VARCHAR(7),
#         proprietario VARCHAR(50),
#         num_portas INT,
#         km_rodado INT,
#         qtd_passageiros INT,
#         ano INTEGER,
#         valor INTEGER,
#         motor INT,
#         combustivel VARCHAR(20),
#         meio_locomocao VARCHAR(30)        
        
# );               
# """)

print('Tabela criada com sucesso.')
conn.close()

class Veiculo: 

    def __init__(self, nome, marca, modelo, cor, placa, proprietario, num_portas, km_rodado, 
                qtd_passageiros, ano, valor, motor, combustivel, meio_locomocao):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.cor = cor
        self.nome = nome
        self.placa = placa
        self.proprietario = proprietario
        self.num_portas = num_portas
        self.km_rodado = km_rodado
        self.qtd_passageiros = qtd_passageiros
        self.motor = motor
        self.combustivel = combustivel
        self.meio_locomocao = meio_locomocao
        

    def salvar_veiculo(self):
        bd = sqlite3.connect('db_veiculos.db')
        sql = bd.cursor()
        
        sql.execute('''
            INSERT INTO veiculos(nome, marca, modelo, cor, placa,
            proprietario, num_portas, km_rodado, qtd_passageiros, ano,
            valor, motor, combustivel, meio_locomocao)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?);''',
            (
                str(self.nome),
                str(self.marca),
                str(self.modelo),
                str(self.cor),
                str(self.placa),
                str(self.proprietario),
                int(self.num_portas),
                int(self.km_rodado),
                int(self.qtd_passageiros),
                int(self.ano),
                float(self.valor),
                float(self.motor),
                str(self.combustivel),
                str(self.meio_locomocao)
            )
        )
        bd.commit()
        bd.close()


def cadastro_veiculo():
    print("\n\t__________CADASTRO DE VEÍCULOS__________\n")
    nome = str(input("Nome do Carro: ")),
    marca = str(input("Marca: ")),
    modelo = input("Modelo: ")
    cor = input("Cor: ")
    placa = input("Placa: ")
    proprietario = input("Nome do proprietário: ")
    num_portas = int(input("Número de portas: "))
    km_rodado = int(input("Km rodado: "))
    qtd_passageiros = int(input("Quantidade máxima de passageiros: "))
    ano = int(input("Ano: "))
    valor = float(input("Valor: R$ "))
    motor = float(input("Motor: "))
    combustivel = input("Tipo de combustível: ")
    meio_locomocao = input("Meio de locomoção: ")
    
    veiculo = Veiculo(nome, marca, modelo, cor, placa, proprietario, num_portas, km_rodado,
                      qtd_passageiros, ano, valor, motor, combustivel, meio_locomocao)  # instancia
    
    veiculo.salvar_veiculo()



cadastro_veiculo()
