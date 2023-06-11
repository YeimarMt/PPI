import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtWidgets import QDesktopWidget, QLabel, QApplication, QMainWindow, QHBoxLayout, QPushButton, QLineEdit, \
    QFormLayout, QWidget, QVBoxLayout, QComboBox, QBoxLayout, QCalendarWidget, QProgressBar, QMessageBox

from ventana4 import Ventana4


class Ventana3(QMainWindow):
    def __init__(self, anterior):
        super(Ventana3, self).__init__(anterior)
        self.initUI()

        self.ventanaAnterior = anterior
        self.setWindowTitle("AGENDAR")

        self.ancho = 800
        self.alto = 600
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

        self.titulo1 = QLabel("AGENDAR CITA", self)

        # Establecemos la posición y el tamaño de la etiqueta
        self.titulo1.setGeometry(410, 120, 100, 20)
        self.titulo1.setAlignment(Qt.AlignCenter)
        self.titulo1.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 16)
        self.titulo1.setFont(self.font)

        self.campo_texto = QLabel(self)
        self.campo_texto.setText("Correo:")
        self.campo_texto.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 10)
        self.campo_texto.setFont(self.font)

        # Creamos un objeto QLabel para el campo de texto
        self.campo_texto = QLabel(self)
        self.campo_texto.setText("Nombre:")
        self.campo_texto.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 10)
        self.campo_texto.setFont(self.font)

        # Creamos un objeto QLineEdit para el campo de texto
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Ingrese su nombre...")
        self.line_edit.setStyleSheet("background-color: #A3D0D7 ; color: #000000; border-radius:7px;")
        self.font = QFont("Arial Rounded MT Bold", 9)
        self.line_edit.setFont(self.font)
        self.line_edit.setFixedWidth(200)
        self.line_edit.setFixedHeight(25)

        # Creamos un objeto QLabel para el campo de texto
        self.campo_texto2 = QLabel(self)
        self.campo_texto2.setText("Apellidos:")
        self.campo_texto2.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 10)
        self.campo_texto2.setFont(self.font)

        # Creamos un objeto QLineEdit para el campo de texto
        self.line_edit2 = QLineEdit(self)
        self.line_edit2.setPlaceholderText("Ingrese su apellido...")
        self.line_edit2.setStyleSheet("background-color: #A3D0D7 ; color: #000000; border-radius:7px;")
        self.font = QFont("Arial Rounded MT Bold", 9)
        self.line_edit2.setFont(self.font)
        self.line_edit2.setFixedWidth(200)
        self.line_edit2.setFixedHeight(25)

        # Creamos un objeto QLabel para el campo de texto
        self.campo_texto1 = QLabel(self)
        self.campo_texto1.setText("Fecha de cita:")
        self.campo_texto1.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 10)
        self.campo_texto1.setFont(self.font)

        # Creamos un objeto QLineEdit para el campo de texto
        self.line_edit3 = QLineEdit(self)
        self.line_edit3.setReadOnly(True)
        self.line_edit3.setPlaceholderText("DD/MM/AA")
        self.line_edit3.setStyleSheet("background-color: #A3D0D7 ; color: #000000; border-radius:7px;")
        self.font = QFont("Arial Rounded MT Bold", 9)
        self.line_edit3.setFont(self.font)
        self.line_edit3.setFixedWidth(140)
        self.line_edit3.setFixedHeight(25)

        # Creamos un objeto QLabel para el campo de texto
        self.campo_texto3 = QLabel(self)
        self.campo_texto3.setText("Hora de cita:")
        self.campo_texto3.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 10)
        self.campo_texto3.setFont(self.font)

        # Creamos un objeto QLineEdit para el campo de texto
        self.line_edit4 = QLineEdit(self)
        self.line_edit4.setPlaceholderText("HH:MM")
        self.line_edit4.setStyleSheet("background-color: #A3D0D7 ; color: #000000; border-radius:7px;")
        self.font = QFont("Arial Rounded MT Bold", 9)
        self.line_edit4.setFont(self.font)
        self.line_edit4.setFixedWidth(140)
        self.line_edit4.setFixedHeight(25)

        # Creamos un objeto QLabel para el campo de texto
        self.campo_texto4 = QLabel(self)
        self.campo_texto4.setText("Tipo de corte:")
        self.campo_texto4.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 10)
        self.campo_texto4.setFont(self.font)

        self.lista_desplegable = QComboBox(self)
        self.lista_desplegable.setStyleSheet("background-color: #A3D0D7 ; color: #000000; border-radius:7px;")
        self.font = QFont("Arial Rounded MT Bold", 9)
        self.lista_desplegable.setFont(self.font)
        self.lista_desplegable.addItem("Eliga su corte")
        self.lista_desplegable.addItem("Corte Completo")
        self.lista_desplegable.addItem("Solo barba")
        self.lista_desplegable.addItem("Bases solas")
        self.lista_desplegable.addItem("Cejas")
        self.lista_desplegable.addItem("Barba y corte")
        self.lista_desplegable.setFixedWidth(140)
        self.lista_desplegable.setFixedHeight(25)
        # Agrega más opciones según sea necesario

        #self.lista_desplegable.setGeometry(100, 100, 200, 30)  # Establece la posición y el tamaño del widget

        # Conecta una función para manejar el evento de selección de la lista desplegable
        self.lista_desplegable.currentIndexChanged.connect(self.manejar_seleccion)


        # Creamos un objeto QLabel para el campo de texto
        self.campo_texto5 = QLabel(self)
        self.campo_texto5.setText("Documento:")
        self.campo_texto5.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 10)
        self.campo_texto5.setFont(self.font)

        # Creamos un objeto QLineEdit para el campo de texto
        self.line_edit6 = QLineEdit(self)
        self.line_edit6.setPlaceholderText("Ingrese su documento...")
        self.line_edit6.setStyleSheet("background-color: #A3D0D7 ; color: #000000; border-radius:7px;")
        self.font = QFont("Arial Rounded MT Bold", 9)
        self.line_edit6.setFont(self.font)
        self.line_edit6.setFixedWidth(200)
        self.line_edit6.setFixedHeight(25)

        # Creamos un objeto QLabel para el campo de texto
        self.campo_texto6 = QLabel(self)
        self.campo_texto6.setText("Telefono:")
        self.campo_texto6.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 10)
        self.campo_texto6.setFont(self.font)

        # Creamos un objeto QLineEdit para el campo de texto
        self.line_edit7 = QLineEdit(self)
        self.line_edit7.setPlaceholderText("##########")
        self.line_edit7.setStyleSheet("background-color: #A3D0D7 ; color: #000000; border-radius:7px;")
        self.font = QFont("Arial Rounded MT Bold", 9)
        self.line_edit7.setFont(self.font)
        self.line_edit7.setFixedWidth(150)
        self.line_edit7.setFixedHeight(25)

        # Creamos un objeto QLabel para el campo de texto
        self.campo_texto7 = QLabel(self)
        self.campo_texto7.setText("Barbero:")
        self.campo_texto7.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 10)
        self.campo_texto7.setFont(self.font)

        self.lista_desplegable1 = QComboBox(self)
        self.lista_desplegable1.setStyleSheet("background-color: #A3D0D7 ; color: #000000; border-radius:7px;")
        self.font = QFont("Arial Rounded MT Bold", 9)
        self.lista_desplegable1.setFont(self.font)
        self.lista_desplegable1.addItem("Eliga barbero")
        self.lista_desplegable1.addItem("Barbero 1")
        self.lista_desplegable1.addItem("Barbero 2")
        self.lista_desplegable1.addItem("Barbero 3")
        self.lista_desplegable1.setFixedWidth(140)
        self.lista_desplegable1.setFixedHeight(25)
        self.lista_desplegable1.currentIndexChanged.connect(self.manejar_seleccion)


        self.boton = QPushButton("Volver", self)
        self.boton.setStyleSheet("background-color: #A3D0D7; color: #000000; padding:7px;"
                                  "border-radius:5px;")
        self.font = QFont("Arial Rounded MT Bold", 10)
        self.boton.setFont(self.font)
        self.boton.setFixedHeight(30)
        self.boton.setFixedWidth(70)
        self.boton.setCursor(Qt.PointingHandCursor)
        self.boton.enterEvent = lambda event: self.boton.setStyleSheet(
            "background-color: #A3D0D7; color: #000000; padding:7px;"
            "border-radius:5px;")
        self.boton.leaveEvent = lambda event: self.boton.setStyleSheet(
            "background-color: #A3D0D7; color: #000000; padding:7px;"
            "border-radius:5px;")
        self.boton.clicked.connect(self.on_Button_Clicked_volver)

        self.boton1 = QPushButton("Ingresar", self)
        self.boton1.setStyleSheet("background-color: #A3D0D7; color: #000000; padding:7px;"
                                 "border-radius:5px;")
        self.font = QFont("Arial Rounded MT Bold", 10)
        self.boton1.setFont(self.font)
        self.boton1.setFixedHeight(30)
        self.boton1.setFixedWidth(70)
        self.boton1.setCursor(Qt.PointingHandCursor)
        self.boton1.enterEvent = lambda event: self.boton1.setStyleSheet(
            "background-color: #A3D0D7; color: #000000; padding:7px;"
            "border-radius:5px;")
        self.boton1.leaveEvent = lambda event: self.boton1.setStyleSheet(
            "background-color: #A3D0D7; color: #000000; padding:7px;"
            "border-radius:5px;")
        self.boton1.clicked.connect(self.guardar_datos)


        self.boton2 = QPushButton("Limpiar", self)
        self.boton2.setStyleSheet("background-color: #A3D0D7; color: #000000; padding:7px;"
                                  "border-radius:5px;")
        self.font = QFont("Arial Rounded MT Bold", 10)
        self.boton2.setFont(self.font)
        self.boton2.setFixedHeight(30)
        self.boton2.setFixedWidth(70)
        self.boton2.setCursor(Qt.PointingHandCursor)
        self.boton2.enterEvent = lambda event: self.boton2.setStyleSheet(
            "background-color: #A3D0D7; color: #000000; padding:7px;"
            "border-radius:5px;")
        self.boton2.leaveEvent = lambda event: self.boton2.setStyleSheet(
            "background-color: #A3D0D7; color: #000000; padding:7px;"
            "border-radius:5px;")
        self.boton2.clicked.connect(self.on_Button_Clicked_limpiar)



        self.label = QLabel(self)
        self.pixmap = QPixmap("Imagenes/logo1.png")  # Reemplaza con la ruta de tu imagen
        self.label.setPixmap(self.pixmap)
        self.label.setAlignment(Qt.AlignCenter)  # Alinea la imagen al centro
        self.label.setStyleSheet("margin: 10px;")  # Agrega un margen de 20 píxeles alrededor de la imagen
        self.label.setGeometry(0, 0, self.pixmap.width(), self.pixmap.height())

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.boton)
        self.hbox.addSpacing(10)  # Agregar espacio de 10 píxeles entre los botones
        self.hbox.addWidget(self.boton1)
        self.hbox.addSpacing(10)  # Agregar espacio de 10 píxeles entre los botones
        self.hbox.addWidget(self.boton2)

        self.form_layout = QFormLayout()
        self.form_layout.setVerticalSpacing(10)  # Establecer espaciado vertical de 10 píxeles

        self.form_layout.addRow(self.titulo1)

        self.form_layout.addRow(self.label)
        self.espacioBlanco = QLabel("")

        self.form_layout.addRow(self.campo_texto5, self.line_edit6)
        self.espacioBlanco = QLabel("")

        self.form_layout.addRow(self.campo_texto, self.line_edit)
        self.espacioBlanco = QLabel("")

        self.form_layout.addRow(self.campo_texto2, self.line_edit2)
        self.espacioBlanco = QLabel("")

        self.form_layout.addRow(self.campo_texto6, self.line_edit7)
        self.espacioBlanco = QLabel("")

        self.form_layout.addRow(self.campo_texto1, self.line_edit3)
        self.espacioBlanco = QLabel("")

        self.form_layout.addRow(self.campo_texto3, self.line_edit4)
        self.espacioBlanco = QLabel("")

        self.form_layout.addRow(self.campo_texto4, self.lista_desplegable)
        self.espacioBlanco = QLabel("")

        self.form_layout.addRow(self.campo_texto7, self.lista_desplegable1)
        self.espacioBlanco = QLabel("")

        self.form_layout.addRow(self.hbox)

        self.widget1 = QWidget()
        self.widget1.setLayout(self.form_layout)

        self.calendar_widget = QCalendarWidget()  # Código del calendario
        self.current_date = QDate.currentDate()
        self.calendar_widget.setMinimumDate(QDate(self.current_date.year(), 1, 1))
        self.calendar_widget.setMaximumDate(QDate(self.current_date.year(), 12, 31))
        self.calendar_widget.setGridVisible(True)
        self.calendar_widget.setFixedSize(315,270)
        self.calendar_widget.selectionChanged.connect(self.actualizar_fecha)
        self.font = QFont("Arial Rounded MT Bold", 9)
        self.calendar_widget.setFont(self.font)
        self.calendar_widget.setStyleSheet("Background-color:#FFFFFF; color:#000000;border: 1px solid #000000;")



        self.main_layout = QHBoxLayout()  # Cambiamos a QHBoxLayout para colocar el formulario y el calendario en una misma línea

        self.main_layout.addWidget(self.widget1)
        self.main_layout.addStretch(1)  # Agregamos un espacio elástico para separar el formulario del calendario

        self.main_layout.addWidget(self.calendar_widget)  # Agregamos el calendario

        self.widget_central = QWidget()
        self.widget_central.setLayout(self.main_layout)

        # Establecemos el layout principal en la ventana
        self.setCentralWidget(self.widget_central)


    def actualizar_fecha(self):
        # Obtiene la fecha seleccionada y la muestra en el QLabel
        fecha = self.calendar_widget.selectedDate()
        fecha_str = fecha.toString("dd/MM/yyyy")
        self.line_edit3.setText(fecha_str)

    def on_Button_Clicked_volver(self):
        self.hide()
        self.ventanaAnterior.show()

    def guardar_datos(self):
        # Obtiene el texto ingresado en los cuadros de texto
        self.texto1 = self.line_edit.text()
        self.texto2 = self.line_edit2.text()
        self.texto3 = self.line_edit3.text()
        self.texto4 = self.line_edit4.text()
        self.texto5 = self.lista_desplegable.currentText()
        self.texto6 = self.line_edit6.text()
        self.texto7 = self.line_edit7.text()
        self.texto8 = self.lista_desplegable1.currentText()

        # Verifica si los campos están vacíos
        if self.texto1 == "" or self.texto2 == "" or self.texto3 == "" or self.texto4 == "" or self.texto5 == "" or self.texto6 == "" or self.texto7 == "" or self.texto8 == "":
            # Mostrar mensaje de campos vacíos
            QMessageBox.warning(self, "Campos Vacíos", "Por favor, complete todos los campos.")
        else:
            # Guarda los datos en un archivo de texto
            with open("clientes.txt", "a") as archivo:
                archivo.write(self.texto6 + ",")
                archivo.write(self.texto1 + ",")
                archivo.write(self.texto2 + ",")
                archivo.write(self.texto3 + ",")
                archivo.write(self.texto4 + ",")
                archivo.write(self.texto5 + ",")
                archivo.write(self.texto7 + ",")
                archivo.write(self.texto8 + "\n")

                # Limpiar los campos
                self.line_edit.clear()
                self.line_edit2.clear()
                self.line_edit3.clear()
                self.line_edit4.clear()
                # Restablecer el valor seleccionado en la lista desplegable
                self.lista_desplegable.setCurrentIndex(0)
                self.line_edit6.clear()
                self.line_edit7.clear()
                self.lista_desplegable1.setCurrentIndex(0)

            # Mostrar mensaje de datos guardados exitosamente
            QMessageBox.information(self, "Datos Guardados", "Los datos han sido guardados correctamente.")



    def on_Button_Clicked_limpiar(self):
        self.line_edit.clear()
        self.line_edit2.clear()
        self.line_edit3.clear()
        self.line_edit4.clear()
        self.line_edit6.clear()
        self.line_edit7.clear()
        self.lista_desplegable.setCurrentIndex(0)



    def initUI(self):
        self.setWindowTitle('Ventana3')
        self.setWindowIcon(QIcon('Imagenes/logo1.png.'))

    def manejar_seleccion(self, index):
        pass

if __name__ == '__ventana3__':
    app = QApplication(sys.argv)
    ventana3 = Ventana3()
    ventana3.show()
    sys.exit(app.exec_())