import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eliminar línea de datos")
        self.setGeometry(100, 100, 300, 200)

        # Crear una etiqueta y un botón
        self.label = QLabel("Presiona el botón 'Eliminar' para borrar la línea de datos.")
        self.button = QPushButton("Eliminar")
        self.button.clicked.connect(self.on_Button_Clicked_eliminar)

        # Crear un diseño vertical y agregar los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Crear un widget central y establecer el diseño
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_Button_Clicked_eliminar(self):
        # Archivo de datos
        archivo = "clientes.txt"

        # Datos a buscar y eliminar
        datos_a_eliminar = [
            self.line_edit.text(),
            self.line_edit2.text(),
            self.line_edit3.text(),
            self.line_edit4.text(),
            self.lista_desplegable.currentText(),
            self.line_edit6.text(),
            self.line_edit7.text(),
            self.lista_desplegable1.currentText()
        ]

        # Leer el archivo y guardar las líneas en una lista
        with open(archivo, "r") as file:
            lineas = file.readlines()

        # Buscar y eliminar las líneas que contienen los datos
        lineas_actualizadas = [linea for linea in lineas if not any(dato in linea for dato in datos_a_eliminar)]

        # Verificar si se encontraron líneas para eliminar
        if len(lineas_actualizadas) < len(lineas):
            # Escribir las líneas actualizadas en el archivo
            with open(archivo, "w") as file:
                file.writelines(lineas_actualizadas)

            self.label.setText("La(s) línea(s) ha(n) sido eliminada(s).")
        else:
            self.label.setText("No se encontraron líneas con los datos proporcionados.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())






    #self.line_edit.text()
    #self.line_edit2.text()
    #self.line_edit3.text()
    #self.line_edit4.text()
    #self.lista_desplegable.currentText()
    #self.line_edit6.text()
    #self.line_edit7.text()
    #self.lista_desplegable1.currentText()
