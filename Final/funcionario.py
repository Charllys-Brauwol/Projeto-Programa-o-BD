from PyQt5 import  uic,QtWidgets
import sqlite3


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
   
app=QtWidgets.QApplication([])
tela_funcionarios=uic.loadUi("cadastrar_funcionario.ui")
tela_funcionarios_2 = uic.loadUi("listarfuncionario.ui")
tela_funcionarios.pushButton.clicked.connect(salvar_dados_funcionarios)
tela_funcionarios.pushButton_2.clicked.connect(listar_dados_funcionarios)

app.exec()


