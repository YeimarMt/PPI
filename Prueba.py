import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Eliminar línea de archivo plano')
        self.setGeometry(200, 200, 400, 200)

        # Crear los elementos de la interfaz de usuario
        self.label = QLabel('Ingrese el dato a buscar:', self)
        self.label.setGeometry(20, 20, 200, 30)

        self.line_edit6 = QLineEdit(self)
        self.line_edit6.setGeometry(220, 20, 150, 30)

        self.search_button = QPushButton('Buscar', self)
        self.search_button.setGeometry(20, 70, 100, 30)
        self.search_button.clicked.connect(self.search_data)

        self.delete_button = QPushButton('Eliminar', self)
        self.delete_button.setGeometry(140, 70, 100, 30)
        self.delete_button.clicked.connect(self.confirm_delete_data)

        self.result_label = QLabel('', self)
        self.result_label.setGeometry(20, 120, 350, 30)

        self.data_eliminar = None  # Variable para almacenar el dato a eliminar

    def search_data(self):
        documento = self.line_edit6.text()
        # Implementa aquí la lógica para buscar la línea en el archivo plano
        # y almacena el dato a eliminar en la variable 'data_to_delete'
        self.data_eliminar = documento  # Ejemplo: se almacena en la variable 'data_to_delete'


    def confirm_delete_data(self):
        if self.data_eliminar:
            confirm_dialog = QMessageBox.question(self, 'Confirmar eliminación', '¿Estás seguro de que deseas eliminar este cliente?', QMessageBox.Yes | QMessageBox.No)
            if confirm_dialog == QMessageBox.Yes:
                self.eliminar_data()
        else:
            self.result_label.setText('Primero debes buscar un dato')

    def on_Button_Clicked_eliminar(self):
        # Ruta al archivo plano
        file_path = 'clientes.txt'

        try:
            # Abrir el archivo en modo lectura
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Abrir el archivo en modo escritura y sobrescribir los datos
            with open(file_path, 'w') as file:
                for line in lines:
                    if self.data_eliminar not in line:
                        file.write(line)

            self.result_label.setText('Línea eliminada: ' + self.data_eliminar)
            self.data_eliminar = None

        except FileNotFoundError:
            self.result_label.setText('Archivo no encontrado')
        except IOError:
            self.result_label.setText('Error al acceder al archivo')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
