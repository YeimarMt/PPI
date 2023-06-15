import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class Ventana4(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear la tabla
        self.table = QTableWidget(self)
        self.setCentralWidget(self.table)

        # Leer los datos del archivo
        self.datos = self.leer_archivo('clientes.txt')

        # Configurar la tabla
        self.table.setRowCount(len(self.datos))
        self.table.setColumnCount(8)  # Supongamos que tienes 3 columnas en tu archivo

        # Establecer encabezados de columna
        encabezados = ['Documento ', 'Nombre', 'Apellidos', '']
        self.table.setHorizontalHeaderLabels(encabezados)

        # Llenar la tabla con los datos
        for i, fila in enumerate(self.datos):
            for j, columna in enumerate(fila):
                item = QTableWidgetItem(columna)
                self.table.setItem(i, j, item)

    def leer_archivo(self, archivo):
        # Leer el archivo y devolver los datos como una lista de filas
        with open(archivo, 'r') as file:
            datos = [linea.strip().split('\t') for linea in file]
        return datos


