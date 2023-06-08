import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDesktopWidget, QLabel, QApplication, QMainWindow, QVBoxLayout, QTextEdit


class Ventana4(QMainWindow):
    def __init__(self, citas):
        super().__init__()
        self.citas = citas
        self.initUI()

        self.setWindowTitle("CONSULTAR")

        self.ancho = 500
        self.alto = 500
        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.setStyleSheet("background-color: #DBEBF6; ")

        #Establecemos el fondo pricipal
        self.fondo = QLabel(self)

        # Estabelecemos la ventana de fondo con la venta central
        self.setCentralWidget(self.fondo)

    def initUI(self):
        layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

        # Mostrar los datos de las citas en el widget de texto
        self.mostrar_citas()


def mostrar_citas(self):
    for cita in self.citas:
        texto_cita = ", ".join(cita)
        self.text_edit.append(texto_cita)

    def initUI(self):
        self.setWindowTitle('Ventana4')
        self.setWindowIcon(QIcon('Imagenes/logo1.png.'))


if __name__ == '__ventana4__':
    app = QApplication(sys.argv)
    ventana4 = Ventana4()
    ventana4.show()
    sys.exit(app.exec_())