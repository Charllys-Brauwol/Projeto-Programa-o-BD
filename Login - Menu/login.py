from PyQt5 import  uic,QtWidgets
import sqlite3


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


app=QtWidgets.QApplication([])
tela_login = uic.loadUi("login.ui")
tela_menu = uic.loadUi("Menu.ui")
tela_login.pushButton.clicked.connect(login)

tela_login.show()
app.exec()


