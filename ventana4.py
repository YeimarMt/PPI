import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDesktopWidget, QLabel, QApplication, QMainWindow


class Ventana4(QMainWindow):
    def __init__(self, parent=None):
        super(Ventana4, self).__init__(parent)
        self.initUI()

        self.setWindowTitle("RECORDATORIO")

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
        self.setWindowTitle('Ventana4')
        self.setWindowIcon(QIcon('Imagenes/logo1.png.'))


if __name__ == '__ventana4__':
    app = QApplication(sys.argv)
    ventana4 = Ventana4()
    ventana4.show()
    sys.exit(app.exec_())