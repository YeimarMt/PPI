import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QPalette, QColor
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QFormLayout, QLineEdit, QVBoxLayout, \
    QSizePolicy, QGraphicsOpacityEffect, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from ventana2 import Ventana2


class Ventana1(QMainWindow):
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)
        self.initUI()


        self.setWindowTitle("¡BIENVENIDO!")

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
        # AED6F1
        #DBEBF6

        #Establecemos el fondo pricipal
        self.fondo = QLabel(self)

        # Estabelecemos la ventana de fondo con la venta central
        self.setCentralWidget(self.fondo)

        self.titulo1 = QLabel("THE CLASSIC CUT", self)

        # Establecemos la posición y el tamaño de la etiqueta
        self.titulo1.setGeometry(410, 120, 100, 20)
        self.titulo1.setAlignment(Qt.AlignCenter)
        self.titulo1.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 16)
        self.titulo1.setFont(self.font)

        self.titulo = QLabel("INICIO DE SESIÓN", self)

        # Establecemos la posición y el tamaño de la etiqueta
        self.titulo.setGeometry(410, 120, 100, 20)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 16)
        self.titulo.setFont(self.font)

        # Creamos un objeto QLabel para el campo de texto
        self.campo_texto = QLabel(self)
        self.campo_texto.setText("Usuario:")
        self.campo_texto.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 10)
        self.campo_texto.setFont(self.font)

        # Creamos un objeto QLineEdit para el campo de texto
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Ingresa usuario...")
        self.line_edit.setStyleSheet("background-color: #A3D0D7 ; color: #000000; border-radius:7px;")
        self.font = QFont("Arial Rounded MT Bold", 9)
        self.line_edit.setFont(self.font)
        self.line_edit.setFixedWidth(150)
        self.line_edit.setFixedHeight(25)

        # Creamos un objeto QLabel para el campo de texto
        self.campo_texto2 = QLabel(self)
        self.campo_texto2.setText("Contraseña:")
        self.campo_texto2.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 10)
        self.campo_texto2.setFont(self.font)

        # Creamos un objeto QLineEdit para el campo de texto
        self.line_edit2 = QLineEdit(self)
        self.line_edit2.setPlaceholderText("Ingresa contraseña...")
        self.line_edit2.setStyleSheet("background-color: #A3D0D7 ; color: #000000; border-radius:7px;")
        self.font = QFont("Arial Rounded MT Bold", 9)
        self.line_edit2.setFont(self.font)
        self.line_edit2.setFixedWidth(150)
        self.line_edit2.setFixedHeight(25)
        self.line_edit2.setEchoMode(QLineEdit.Password)

        self.boton = QPushButton("Ingresar", self)
        self.boton.setStyleSheet("background-color: #A3D0D7; color: #000000; padding:7px;"
                                "border-radius:5px;")
        self.font = QFont("Arial Rounded MT Bold", 9)
        self.boton.setFont(self.font)
        self.boton.setFixedHeight(30)
        self.boton.setCursor(Qt.PointingHandCursor)
        self.boton.enterEvent = lambda event: self.boton.setStyleSheet(
                                "background-color: #A3D0D7; color: #000000; padding:7px;"
                                "border-radius:5px;")
        self.boton.leaveEvent = lambda event: self.boton.setStyleSheet(
                                "background-color: #A3D0D7; color: #000000; padding:7px;"
                                "border-radius:5px;")
        self.boton.clicked.connect(self.on_button_clicked)

        self.label = QLabel(self)
        self.pixmap = QPixmap("Imagenes/logo1.png")  # Reemplaza con la ruta de tu imagen
        self.label.setPixmap(self.pixmap)
        self.label.setAlignment(Qt.AlignCenter)  # Alinea la imagen al centro
        self.label.setStyleSheet("margin: 10px;")  # Agrega un margen de 20 píxeles alrededor de la imagen
        self.label.setGeometry(0, 0,self.pixmap.width(), self.pixmap.height())

        # Creamos un objeto QFormLayout y lo agregamos al layout principal
        self.form_layout = QFormLayout()
        self.form_layout.addRow(self.titulo1)
        self.espacioBlanco = QLabel("")
        self.form_layout.addRow(self.espacioBlanco)
        self.espacioBlanco = QLabel("")
        self.form_layout.addRow(self.espacioBlanco)
        self.form_layout.addRow(self.label)
        self.espacioBlanco = QLabel("")
        self.form_layout.addRow(self.espacioBlanco)
        self.form_layout.addRow(self.titulo)
        self.espacioBlanco = QLabel("")
        self.form_layout.addRow(self.espacioBlanco)
        self.form_layout.addRow(self.campo_texto, self.line_edit)
        self.espacioBlanco = QLabel("")
        self.form_layout.addRow(self.campo_texto2, self.line_edit2)
        self.espacioBlanco = QLabel("")
        self.form_layout.addRow(self.boton)


        self.widget1 = QWidget()
        self.widget1.setLayout(self.form_layout)
        # Aplicar el estilo CSS para agregar un borde


        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.widget1, alignment=Qt.AlignCenter)

        self.main_layout.setAlignment(Qt.AlignCenter)


        self.widget_central = QWidget()
        self.widget_central.setLayout(self.main_layout)

        # Establecemos el layout principal en la ventana
        self.setCentralWidget(self.widget_central)



    def on_button_clicked(self):
        usuario = self.line_edit.text()
        contrasena = self.line_edit2.text()

        if self.verificar_usuario(usuario, contrasena):
            self.hide()
            self.ventana2 = Ventana2(self)
            self.ventana2.show()
        else:
            self.message_box = QMessageBox()
            self.message_box.setWindowTitle("Error")
            self.message_box.setStyleSheet("background-color: #DBEBF6; color: #000000")
            self.message_box.setText("Usuario o contraseña incorrectos.\nIntenta de nuevo.")
            self.font = QFont("Arial Rounded MT Bold")
            self.message_box.setFont(self.font)
            self.message_box.setIcon(QMessageBox.Warning)
            self.ok_button = self.message_box.addButton(QMessageBox.Ok)
            self.ok_button.setStyleSheet("background-color: #85C1E9; color: #000000; padding:7px; border-radius:5px;")
            self.font = QFont("Arial Rounded MT Bold")
            self.ok_button.setFont(self.font)
            self.ok_button.setCursor(Qt.PointingHandCursor)
            self.message_box.exec_()

    def verificar_usuario(self, usuario, contrasena):
        admin1 = {
            "usuario": "",
            "contrasena": ""
        }

        if usuario == admin1["usuario"] and contrasena == admin1["contrasena"]:
            return True
        else:
            return False


    def initUI(self):
        self.setWindowTitle('Ventana1')
        self.setWindowIcon(QIcon('Imagenes/logo1.png'))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana1 = Ventana1()
    ventana1.show()
    sys.exit(app.exec_())













