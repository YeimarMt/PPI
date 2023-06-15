import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Búsqueda de Clientes")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()
        self.documento_label = QLabel("Documento:")
        self.documento_input = QLineEdit()
        self.buscar_button = QPushButton("Buscar")
        self.buscar_button.clicked.connect(self.on_Button_Clicked_buscar)

        self.nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        self.apellido_label = QLabel("Apellido:")
        self.apellido_input = QLineEdit()
        self.direccion_label = QLabel("Dirección:")
        self.direccion_input = QLineEdit()
        self.campo4_label = QLabel("Campo 4:")
        self.campo4_input = QLineEdit()
        self.campo5_label = QLabel("Campo 5:")
        self.campo5_input = QLineEdit()
        self.campo6_label = QLabel("Campo 6:")
        self.campo6_combobox = QComboBox()
        self.campo7_label = QLabel("Campo 7:")
        self.campo7_combobox = QComboBox()

        layout.addWidget(self.documento_label)
        layout.addWidget(self.documento_input)
        layout.addWidget(self.buscar_button)
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.apellido_label)
        layout.addWidget(self.apellido_input)
        layout.addWidget(self.direccion_label)
        layout.addWidget(self.direccion_input)
        layout.addWidget(self.campo4_label)
        layout.addWidget(self.campo4_input)
        layout.addWidget(self.campo5_label)
        layout.addWidget(self.campo5_input)
        layout.addWidget(self.campo6_label)
        layout.addWidget(self.campo6_combobox)
        layout.addWidget(self.campo7_label)
        layout.addWidget(self.campo7_combobox)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Agregar opciones a las listas desplegables
        self.campo6_combobox.addItems(["Opción 1", "Opción 2", "Opción 3"])
        self.campo7_combobox.addItems(["Opción A", "Opción B", "Opción C"])

    def on_Button_Clicked_buscar(self):
        documento = self.documento_input.text()

        # Realizar la búsqueda en el archivo plano
        with open("clientes.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == documento:
                    # Si se encuentra el documento, rellenar el formulario
                    self.nombre_input.setText(data[1])
                    self.apellido_input.setText(data[2])
                    self.direccion_input.setText(data[3])
                    self.campo4_input.setText(data[4])
                    self.campo5_input.setText(data[5])
                    self.campo6_combobox.setCurrentText(data[6])
                    self.campo7_combobox.setCurrentText(data[7])
                    break  # Terminar el bucle después de encontrar el documento

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
