import sys
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtWidgets import QDesktopWidget, QLabel, QApplication, QMainWindow, QTableWidgetItem, QTableWidget, \
    QFormLayout, QWidget, QVBoxLayout, QHeaderView, QPushButton
from PyQt5.QtCore import Qt
from datetime import datetime


class Ventana6(QMainWindow):
    def __init__(self, ventana_anterior):
        super().__init__()
        self.ventana_anterior = ventana_anterior
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CITAS BARBERO 2')
        self.setWindowIcon(QIcon('Imagenes/logo1.png'))

        self.ancho = 900
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.setStyleSheet("background-color: #DBEBF6; ")

        imagen_label = QLabel(self)
        imagen_label.setPixmap(
            QPixmap('imagenes/logo1.png'))  # Reemplaza 'ruta/a/la/imagen.png' con la ruta correcta de la imagen
        imagen_label.setAlignment(Qt.AlignCenter)

        self.titulo_label = QLabel('CONSULTA', self)
        self.titulo_label.setStyleSheet("color: #000000;")
        self.font = QFont("Arial Rounded MT Bold", 14)
        self.titulo_label.setFont(self.font)
        self.titulo_label.setAlignment(Qt.AlignCenter)


        self.boton = QPushButton("Volver", self)
        self.boton.setStyleSheet("background-color: #A3D0D7; color: #000000; padding:7px;"
                                 "border-radius:5px;")
        self.font = QFont("Arial Rounded MT Bold", 10)
        self.boton.setFont(self.font)
        self.boton.setFixedHeight(40)
        self.boton.setFixedWidth(100)
        self.boton.setCursor(Qt.PointingHandCursor)
        self.boton.enterEvent = lambda event: self.boton.setStyleSheet(
            "background-color: #A3D0D7; color: #000000; padding:7px;"
            "border-radius:5px;")
        self.boton.leaveEvent = lambda event: self.boton.setStyleSheet(
            "background-color: #A3D0D7; color: #000000; padding:7px;"
            "border-radius:5px;")
        self.boton.clicked.connect(self.on_Button_Clicked_volver)

        # Crear la tabla
        self.table = QTableWidget()



        # Leer los datos del archivo
        self.datos = self.leer_archivo('clientes.txt')

        # Configurar la tabla
        self.table.setRowCount(len(self.datos))
        self.table.setColumnCount(8)  # Supongamos que tienes 8 columnas en tu archivo

        # Establecer encabezados de columna
        self.encabezados = ['Documento', 'Nombre', 'Apellidos', 'Fecha', 'Hora', 'Tipo de corte', 'Telefono', 'Barbero']
        self.table.setHorizontalHeaderLabels(self.encabezados)

        self.header = self.table.horizontalHeader()
        self.header.setStyleSheet("QHeaderView::section { background-color: #A3D0D7; border: 1px solid #000000; }")

        # Llenar la tabla con los datos
        sorted_datos = sorted(self.datos, key=lambda x: datetime.strptime(x[3], '%d/%m/%Y'))
        for i, fila in enumerate(sorted_datos):
            for j, columna in enumerate(fila):
                item = QTableWidgetItem(columna)
                self.table.setItem(i, j, item)

        # Establecer estilo para el borde de los datos
        self.table.setStyleSheet("""
            QTableWidget::item {
                border: 1px solid #000000;
            }
            QTableWidget::item:selected {
                color: #000000;
                background-color: #A3D0D7;
            }
        """)
        # Ajustar el alto de las filas
        self.table.verticalHeader().setDefaultSectionSize(30)  # Alto de las filas
        self.table.horizontalHeader().setDefaultSectionSize(105)

        self.table.resize(600, 100)

        # Permitir que la tabla se ajuste al tamaño de la ventana
        self.table.setSizeAdjustPolicy(QTableWidget.AdjustToContents)

        # Crear un layout vertical y agregar la tabla y el botón
        # Crear un layout vertical y agregar la tabla
        self.layout = QVBoxLayout()
        self.layout.addWidget(imagen_label)
        self.layout.addWidget(self.titulo_label)
        self.layout.addWidget(self.table)

        # Crear un layout vertical para el botón
        self.boton_layout = QVBoxLayout()

        self.boton_layout.addWidget(self.boton)
        self.boton_layout.setAlignment(Qt.AlignCenter)

        # Agregar el layout del botón al layout principal
        self.layout.addLayout(self.boton_layout)

        # Crear un widget central y establecer el layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)

        # Establecer el widget central en la ventana
        self.setCentralWidget(self.central_widget)

        self.central_widget.setStyleSheet("border: none;")

    def leer_archivo(self, archivo):
        # Leer el archivo y devolver los datos como una lista de filas
        with open(archivo, 'r') as file:
            self.datos = [linea.strip().split(',') for linea in file]
        return self.datos

    def on_Button_Clicked_volver(self):
        self.ventana_anterior.show()  # Mostrar la ventana anterior
        self.close()  # Cerrar la ventana actual

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana6 = Ventana6()
    ventana6.show()
    sys.exit(app.exec_())