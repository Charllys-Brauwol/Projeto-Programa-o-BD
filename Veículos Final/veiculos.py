from PyQt5 import  uic,QtWidgets
import sqlite3


def listar_dados():
    tela_2.show()
    banco = sqlite3.connect('banco_veiculos.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM dados")
    dados_lidos = cursor.fetchall()
    tela_2.tableWidget.setRowCount(len(dados_lidos))
    tela_2.tableWidget.setColumnCount(2)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 2):
           tela_2.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    banco.close()
    

def salvar_dados():
    veiculo = tela.lineEdit.text()
    placa = tela.lineEdit_2.text()
    
    try:
        banco = sqlite3.connect('banco_veiculos.db') 
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados (veiculo text,placa text)")
        cursor.execute("INSERT INTO dados VALUES ('"+veiculo+"','"+placa+"')")
        banco.commit() 
        banco.close()
        tela.lineEdit.setText("")
        tela.lineEdit_2.setText("")
        print("Dados inseridos com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao inserir os dados: ",erro)
   
app=QtWidgets.QApplication([])
tela=uic.loadUi("cadastrar_veiculos.ui")
tela_2 = uic.loadUi("listarveiculos.ui")
tela.pushButton.clicked.connect(salvar_dados)
tela.pushButton_2.clicked.connect(listar_dados)

tela.show()
app.exec()


