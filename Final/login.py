from PyQt5 import  uic,QtWidgets
import sqlite3

#Tela Principal de Login
def login():
    usuario_digitado = tela_login.lineEdit.text()
    senha_digitada = int(tela_login.lineEdit_2.text())

    banco = sqlite3.connect('banco_login.db') 
    cursor = banco.cursor()
    
    cursor.execute("SELECT senha FROM logins WHERE usuario ='{}'".format(usuario_digitado))
    senha_banco = cursor.fetchall()
    banco.close()
    
    if senha_digitada == senha_banco[0][0] :        
        tela_login.close()
        tela_menu.show()
    else :
        print("Erro")

#Função do Botão de Listar Veículos Cadastrados
def listar_dados_veiculos():
    tela_veiculos_2.show()
    banco = sqlite3.connect('banco_veiculos.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM dados")
    dados_lidos = cursor.fetchall()
    tela_veiculos_2.tableWidget.setRowCount(len(dados_lidos))
    tela_veiculos_2.tableWidget.setColumnCount(2)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 2):
           tela_veiculos_2.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    banco.close()
    
#Função do Botão de Cadastrar Veiculos
def salvar_dados_veiculos():
    tela_veiculos.show()
    veiculo = tela_veiculos.lineEdit.text()
    placa = tela_veiculos.lineEdit_2.text()
    
    try:
        banco = sqlite3.connect('banco_veiculos.db') 
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados (veiculo text,placa text)")
        cursor.execute("INSERT INTO dados VALUES ('"+veiculo+"','"+placa+"')")
        banco.commit() 
        banco.close()
        tela_veiculos.lineEdit.setText("")
        tela_veiculos.lineEdit_2.setText("")
        print("Dados inseridos com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao inserir os dados: ",erro)

#Função do Botão de Inserir Dados de Viagens
def inserir_dados_veiculos():
    tela_menu.close()
    tela_veiculos_4.show()
    km_saida = tela_veiculos_4.lineEdit.float()
    km_volta = tela_veiculos_4.lineEdit_2.float()
    abastecimento = tela_veiculos_4.lineEdit_3.float()
    data_viagem = tela_veiculos_4.lineEdit_4.int()
    posto = tela_veiculos_4.lineEdit_5.text()
    tecnicos_viagem = tela_veiculos_4.lineEdit_6.text()
    localidades = tela_veiculos_4.lineEdit_7.text()

#Função Menu Principal Veículos
def menu_veiculos():
    tela_menu.close()
    tela_veiculos_3.show()

#Função do Botão de Listar Funcionários Cadastrados
def listar_dados_funcionarios():
    tela_funcionarios_2.show()
    banco = sqlite3.connect('banco_funcionario.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM dados")
    dados_lidos = cursor.fetchall()
    tela_funcionarios_2.tableWidget.setRowCount(len(dados_lidos))
    tela_funcionarios_2.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
           tela_funcionarios_2.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    banco.close()
    
#Função do Botão de Cadastrar Funcionarios
def salvar_dados_funcionarios():
    tela_funcionarios.show()
    nome_completo = tela_funcionarios.lineEdit.text()
    rg = tela_funcionarios.lineEdit_2.text()
    cpf = tela_funcionarios.lineEdit_3.text()
    telefone = tela_funcionarios.lineEdit_4.text()
    endereco = tela_funcionarios.lineEdit_5.text()

    try:
        banco = sqlite3.connect('banco_funcionario.db') 
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados (nome_completo text, rg text, cpf text, telefone text, endereco text)")
        cursor.execute("INSERT INTO dados VALUES ('"+nome_completo+"','"+rg+"','"+cpf+"','"+telefone+"','"+endereco+"')")
        banco.commit() 
        banco.close()
        tela_funcionarios.lineEdit.setText("")
        tela_funcionarios.lineEdit_2.setText("")
        tela_funcionarios.lineEdit_3.setText("")
        tela_funcionarios.lineEdit_4.setText("")
        tela_funcionarios.lineEdit_5.setText("")
        print("Dados inseridos com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao inserir os dados: ",erro)

#Função do Botão de Listar Cidades Cadastradas
def listar_dados_cidades():
    tela_cidades_2.show()
    banco = sqlite3.connect('banco_cidades.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM dados")
    dados_lidos = cursor.fetchall()
    tela_cidades_2.tableWidget.setRowCount(len(dados_lidos))
    tela_cidades_2.tableWidget.setColumnCount(3)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
           tela_cidades_2.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    banco.close()
    
#Função do Botão de Cadastrar Cidades
def salvar_dados_cidades():
    tela_cidades.show()
    cidade = tela_cidades.lineEdit.text()
    endereco = tela_cidades.lineEdit_2.text()
    ano = tela_cidades.lineEdit_3.text()
    
    try:
        banco = sqlite3.connect('banco_cidades.db') 
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados (cidade text,endereco text,ano text)")
        cursor.execute("INSERT INTO dados VALUES ('"+cidade+"','"+endereco+"','"+ano+"')")
        banco.commit() 
        banco.close()
        tela_cidades.lineEdit.setText("")
        tela_cidades.lineEdit_2.setText("")
        tela_cidades.lineEdit_3.setText("")
        print("Dados inseridos com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao inserir os dados: ",erro)
   
app=QtWidgets.QApplication([])

#Telas Relacionadas ao Login e Menu Principal
tela_login = uic.loadUi("login.ui")
tela_menu = uic.loadUi("Menu.ui")
tela_login.pushButton.clicked.connect(login)
tela_menu.pushButton.clicked.connect(salvar_dados_funcionarios)
tela_menu.pushButton_2.clicked.connect(menu_veiculos)
tela_menu.pushButton_3.clicked.connect(salvar_dados_cidades)

#Telas Relacionadas aos Veículos
tela_veiculos = uic.loadUi("cadastrar_veiculos.ui")
tela_veiculos_2 = uic.loadUi("listarveiculos.ui")
tela_veiculos_3 = uic.loadUi("menu_veiculos.ui")
tela_veiculos_4 = uic.loadUi("dados_veiculos.ui")
tela_veiculos.pushButton.clicked.connect(salvar_dados_veiculos)
tela_veiculos.pushButton_2.clicked.connect(listar_dados_veiculos)
tela_veiculos_3.pushButton.clicked.connect(salvar_dados_veiculos)
tela_veiculos_3.pushButton_2.clicked.connect(inserir_dados_veiculos)

#Telas relacionadas aos Funcionários
tela_funcionarios=uic.loadUi("cadastrar_funcionario.ui")
tela_funcionarios_2 = uic.loadUi("listarfuncionario.ui")
tela_funcionarios.pushButton.clicked.connect(salvar_dados_funcionarios)
tela_funcionarios.pushButton_2.clicked.connect(listar_dados_funcionarios)

#Telas Relacionadas as Cidades
tela_cidades=uic.loadUi("cadastrar_cidades.ui")
tela_cidades_2 = uic.loadUi("listarcidades.ui")
tela_cidades.pushButton.clicked.connect(salvar_dados_cidades)
tela_cidades.pushButton_2.clicked.connect(listar_dados_cidades)

tela_login.show()
app.exec()