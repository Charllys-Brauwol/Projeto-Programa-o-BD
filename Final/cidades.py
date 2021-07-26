from PyQt5 import  uic,QtWidgets
import sqlite3


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
tela_cidades=uic.loadUi("cadastrar_cidades.ui")
tela_cidades_2 = uic.loadUi("listarcidades.ui")
tela_cidades.pushButton.clicked.connect(salvar_dados_cidades)
tela_cidades.pushButton_2.clicked.connect(listar_dados_cidades)

app.exec()


