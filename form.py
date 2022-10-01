from PyQt5 import uic, QtWidgets
import mysql.connector


def apresentarFormulario():
    return uic.loadUi("formulario.ui")


def listarDados():
    return uic.loadUi("listar_dados.ui")


def conectarBanco():
    return mysql.connector.connect(
        host="localhost", user="root", passwd="rapadura321", database="cadastro_usuario"
    )


def inserirBanco():
    lista = [
        form.lineEdit.text(),
        form.lineEdit_2.text(),
        form.lineEdit_3.text(),
        form.lineEdit_4.text(),
    ]

    banco = conectarBanco()
    cursor = banco.cursor()
    comandoSQL = f"INSERT INTO usuario (nome,email,cidade,senha) VALUES ('{lista[0]}','{lista[1]}','{lista[2]}','{lista[3]}')"
    cursor.execute(comandoSQL)
    banco.commit()
    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    form = apresentarFormulario()
    form.show()
    form.pushButton_2.clicked.connect(inserirBanco)
    form.pushButton_2.clicked.connect(exit)
    form.pushButton.clicked.connect(exit)

    app.exec()
