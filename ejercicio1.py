import sys
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciarUI()
        self.show() #linea obligatoria

    def iniciarUI(self):

        #definir ventana
        self.setGeometry(300,200,400,200)
        self.setWindowTitle("Ejercicio 1 Seccion Practica Prueba Individual")

        #definir labels
        titulo = QLabel("NOMBRE USUARIO")
        titulo.setAlignment(Qt.AlignmentFlag.AlignLeft)

        imagen = QLabel()
        imagen.setPixmap(QPixmap())
        imagen.setFixedSize(100,100)

        subtexto = QLabel("Texto Descripcion Usuario")

        atributo1 = QLabel("Atributo 1")
        valor1 = QLabel("Valor 1")
        atributo2 = QLabel("Atributo 2")
        valor2 = QLabel("Valor 2")
        atributo3 = QLabel("Atributo 3")
        valor3 = QLabel("Valor 3")
        atributo4 = QLabel("Atributo 4")
        valor4 = QLabel("Valor 4")  
        atributo5 = QLabel("Atributo 5")
        valor5 = QLabel("Valor 5")  
        atributo6 = QLabel("Atributo 6")
        valor6 = QLabel("Valor 6")

        extra1 = QLabel("")
        extra2 = QLabel("")
        botonOk = QPushButton("Ok")

        #definir layouts
        ly_imagen = QVBoxLayout()
        ly_imagen.addWidget(imagen)
        ly_imagen.addWidget(subtexto)

        ly_atributos = QVBoxLayout()
        ly_atributos.addWidget(atributo1)
        ly_atributos.addWidget(atributo2)
        ly_atributos.addWidget(atributo3)
        ly_atributos.addWidget(atributo4)
        ly_atributos.addWidget(atributo5)
        ly_atributos.addWidget(atributo6)

        ly_valores = QVBoxLayout()
        ly_valores.addWidget(valor1)
        ly_valores.addWidget(valor2)
        ly_valores.addWidget(valor3)
        ly_valores.addWidget(valor4)
        ly_valores.addWidget(valor5)
        ly_valores.addWidget(valor6)

        ly_central = QHBoxLayout()
        ly_central.addLayout(ly_imagen)
        ly_central.addLayout(ly_atributos)
        ly_central.addLayout(ly_valores)

        ly_boton = QHBoxLayout()
        ly_boton.addWidget(extra1)
        ly_boton.addWidget(extra2)
        ly_boton.addWidget(botonOk)

        main_ly = QVBoxLayout()
        main_ly.addWidget(titulo)
        main_ly.addLayout(ly_central)
        main_ly.addLayout(ly_boton)

        self.setLayout(main_ly)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())