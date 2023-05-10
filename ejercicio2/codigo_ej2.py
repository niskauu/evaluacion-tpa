import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

from VentanaPrincipal import Ui_VentanaPrincipal
from VentanaSecundaria import Ui_VentanaSecundaria

class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, peso:float):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def __str__(self) -> str:
        return f"Mascota {self.nombre} de {self.edad} anios de la especie {self.especie} con {self.peso} Kg."


class Ventana(QtWidgets.QMainWindow, Ui_VentanaPrincipal, Ui_VentanaSecundaria):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)
        # self.setupUi2(self)

        self.pushButton.clicked.connect(self.guardar_mascota)
        
    def guardar_mascota(self):
        nombre_input = self.entrada_nombre.text()
        especie_input = self.entrada_especie.text()
        edad_input = self.entrada_edad
        peso_input = self.entrada_peso
        if len(nombre_input) != 0 and len(especie_input) != 0:
            mascota = Mascota(nombre_input, especie_input, edad_input, peso_input)
            self.ventana_secundaria()
        else:
            QMessageBox.warning(self, "Error",
            "Falta ingresar Datos de la mascota",
            QMessageBox.StandardButton.Ok,
            QMessageBox.StandardButton.Ok)

    # no pude implementar segunda ventana
    # def ventana_secundaria():
    #     self.setupUi2.show()

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    vista = Ventana()
    vista.show()
    app.exec()