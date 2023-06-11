import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QLabel, QApplication, QFormLayout, QWidget, QVBoxLayout, \
    QHBoxLayout, QPushButton


from ventana3 import Ventana3
from ventana4 import Ventana4



class Ventana2(QMainWindow):
    def __init__(self, anterior):
        super(Ventana2, self).__init__()
        self.initUI()

        self.ventanaAnterior = anterior

        self.setWindowTitle("MENU PRINCIPAL")

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
        # Establecemos el fondo principal
        self.fondo = QLabel(self)

        self.titulo1 = QLabel("THE CLASSIC CUT", self)
        self.titulo1.setAlignment(Qt.AlignHCenter)
        self.titulo1.setGeometry(200, 30, 400, 400)
        self.titulo1.setFixedWidth(200)
        self.titulo1.setFixedHeight(25)
        self.titulo1.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 14)
        self.titulo1.setFont(self.font)

        # AED6F1
        self.titulo = QLabel("AGENDAR", self)
        self.titulo.setAlignment(Qt.AlignHCenter)
        self.titulo.setGeometry(15, 400, 20, 20)
        self.titulo.setFixedWidth(200)
        self.titulo.setFixedHeight(25)
        self.titulo.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 14)
        self.titulo.setFont(self.font)


        self.titulo1 = QLabel("CONSULTAR", self)
        self.titulo1.setAlignment(Qt.AlignHCenter)
        self.titulo1.setGeometry(205, 400, 400, 400)
        self.titulo1.setFixedWidth(200)
        self.titulo1.setFixedHeight(25)
        self.titulo1.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 14)
        self.titulo1.setFont(self.font)

        self.titulo2 = QLabel("CANCELAR", self)
        self.titulo2.setAlignment(Qt.AlignHCenter)
        self.titulo2.setGeometry(395, 400, 400, 400)
        self.titulo2.setFixedWidth(200)
        self.titulo2.setFixedHeight(25)
        self.titulo2.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 14)
        self.titulo2.setFont(self.font)

        self.boton = QPushButton("", self)
        #self.boton.setStyleSheet("background-color: #2E86C1; color: #FFFFFF; padding:7px;"
                                 #"border-radius:5px;")
        self.boton.setFont(self.font)
        self.boton.setFixedHeight(150)
        self.boton.setFixedWidth(150)
        self.boton.setStyleSheet("QPushButton { border-image: url(Imagenes/Caramelo.png)}")
        self.boton.setCursor(Qt.PointingHandCursor)
        self.boton.setGeometry(40, 220, 400, 400)
        self.boton.clicked.connect(self.on_Button_Clicked)

        self.boton1 = QPushButton("", self)
        #self.boton1.setStyleSheet("background-color: #2E86C1; color: #FFFFFF; padding:7px;"
                                 #"border-radius:5px;")
        self.boton1.setFont(self.font)
        self.boton1.setFixedHeight(150)
        self.boton1.setFixedWidth(150)
        self.boton1.setStyleSheet("QPushButton { border-image: url(Imagenes/Consultar.png)}")
        self.boton1.setCursor(Qt.PointingHandCursor)
        self.boton1.setGeometry(230, 220, 400, 400)
        self.boton1.clicked.connect(self.on_Button_Clicked1)

        self.boton3 = QPushButton("", self)
        # self.boton.setStyleSheet("background-color: #2E86C1; color: #FFFFFF; padding:7px;"
        # "border-radius:5px;")
        self.boton3.setFont(self.font)
        self.boton3.setFixedHeight(150)
        self.boton3.setFixedWidth(150)
        self.boton3.setStyleSheet("QPushButton { border-image: url(Imagenes/Caancelar.png)}")
        self.boton3.setCursor(Qt.PointingHandCursor)
        self.boton3.setGeometry(415, 220, 400, 400)

        self.boton4 = QPushButton("", self)
        # self.boton.setStyleSheet("background-color: #2E86C1; color: #FFFFFF; padding:7px;"
        # "border-radius:5px;")
        self.boton4.setFont(self.font)
        self.boton4.setFixedHeight(100)
        self.boton4.setFixedWidth(100)
        self.boton4.setStyleSheet("QPushButton { border-image: url(Imagenes/logo1.png)}")
        self.boton4.setGeometry(250, 65, 400, 400)



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
            self.ventana3 = Ventana3(self)
            self.ventana3.show()

    def on_Button_Clicked1(self):
            self.hide()
            self.ventana4 = Ventana4(self)
            self.ventana4.show()


    def on_Button_Clicked2(self):
        self.hide()
        self.ventanaAnterior.show()


    def initUI(self):
        self.setWindowTitle('Ventana2')
        self.setWindowIcon(QIcon('Imagenes/logo1.png'))

if __name__ == '__ventana2__':
    app = QApplication(sys.argv)
    ventana2 = Ventana2()
    ventana2.show()
    sys.exit(app.exec_())