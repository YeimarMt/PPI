import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QLabel, QPushButton

from ventana6 import Ventana6
from ventana5 import Ventana5


class Ventana4(QMainWindow):
    def __init__(self, ventana_anterior):
        super().__init__()
        self.ventana_anterior = ventana_anterior
        self.initUI()

        self.setWindowTitle("ELIGE BARBERO")

        self.ancho = 600
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.setStyleSheet("background-color: #DBEBF6; ")

        self.fondo = QLabel(self)

        self.titulo1 = QLabel("ELIGE BARBERO", self)
        self.titulo1.setAlignment(Qt.AlignHCenter)
        self.titulo1.setGeometry(205, 180, 400, 400)
        self.titulo1.setFixedWidth(200)
        self.titulo1.setFixedHeight(25)
        self.titulo1.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 14)
        self.titulo1.setFont(self.font)

        # AED6F1
        self.titulo = QLabel("BARBERO 1", self)
        self.titulo.setAlignment(Qt.AlignHCenter)
        self.titulo.setGeometry(50, 400, 20, 20)
        self.titulo.setFixedWidth(200)
        self.titulo.setFixedHeight(25)
        self.titulo.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 14)
        self.titulo.setFont(self.font)

        self.titulo1 = QLabel("BARBERO 2", self)
        self.titulo1.setAlignment(Qt.AlignHCenter)
        self.titulo1.setGeometry(365, 400, 400, 400)
        self.titulo1.setFixedWidth(200)
        self.titulo1.setFixedHeight(25)
        self.titulo1.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 14)
        self.titulo1.setFont(self.font)

        self.boton = QPushButton("", self)
        # self.boton.setStyleSheet("background-color: #2E86C1; color: #FFFFFF; padding:7px;"
        # "border-radius:5px;")
        self.boton.setFont(self.font)
        self.boton.setFixedHeight(150)
        self.boton.setFixedWidth(150)
        self.boton.setStyleSheet("QPushButton { border-image: url(imagenes/Barbero1.png)}")
        self.boton.setCursor(Qt.PointingHandCursor)
        self.boton.setGeometry(70, 220, 400, 400)
        self.boton.clicked.connect(self.on_Button_Clicked)

        self.boton1 = QPushButton("", self)
        # self.boton1.setStyleSheet("background-color: #2E86C1; color: #FFFFFF; padding:7px;"
        # "border-radius:5px;")
        self.boton1.setFont(self.font)
        self.boton1.setFixedHeight(150)
        self.boton1.setFixedWidth(150)
        self.boton1.setStyleSheet("QPushButton { border-image: url(imagenes/Barbero2.png)}")
        self.boton1.setCursor(Qt.PointingHandCursor)
        self.boton1.setGeometry(390, 220, 400, 400)
        self.boton1.clicked.connect(self.on_Button_Clicked1)

        self.boton4 = QPushButton("", self)
        # self.boton.setStyleSheet("background-color: #2E86C1; color: #FFFFFF; padding:7px;"
        # "border-radius:5px;")
        self.boton4.setFont(self.font)
        self.boton4.setFixedHeight(100)
        self.boton4.setFixedWidth(100)
        self.boton4.setStyleSheet("QPushButton { border-image: url(Imagenes/logo1.png)}")
        self.boton4.setGeometry(250, 40, 400, 400)

        self.boton2 = QPushButton("Volver", self)
        self.boton2.setStyleSheet("background-color: #85C1E9; color: #000000; padding:7px;"
                                  "border-radius:5px;")
        self.font = QFont("Arial Rounded MT Bold", 10)
        self.boton2.setFont(self.font)
        self.boton2.setFixedHeight(40)
        self.boton2.setFixedWidth(100)
        self.boton2.setGeometry(250, 510, 400, 400)
        self.boton2.setCursor(Qt.PointingHandCursor)
        self.boton2.enterEvent = lambda event: self.boton2.setStyleSheet(
            "background-color: #A3D0D7; color: #000000; padding:7px;"
            "border-radius:5px;")
        self.boton2.leaveEvent = lambda event: self.boton2.setStyleSheet(
            "background-color: #A3D0D7; color: #000000; padding:7px;"
            "border-radius:5px;")
        self.boton2.clicked.connect(self.on_Button_Clicked2)


    def on_Button_Clicked(self):
            self.hide()
            self.ventana5 = Ventana5(self)
            self.ventana5.show()

    def on_Button_Clicked1(self):
            self.hide()
            self.ventana6 = Ventana6(self)
            self.ventana6.show()


    def on_Button_Clicked2(self):
        self.ventana_anterior.show()  # Mostrar la ventana anterior
        self.close()  # C



    def initUI(self):
        self.setWindowTitle('Ventana1')
        self.setWindowIcon(QIcon('Imagenes/logo1.png'))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana4 = Ventana4()
    ventana4.show()
    sys.exit(app.exec_())

