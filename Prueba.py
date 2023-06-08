from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
from PyQt5.QtCore import QTimer, QTime

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reloj")
        self.setGeometry(200, 200, 400, 300)

        # Crea un widget central y un layout vertical para él
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Crea un QLabel para mostrar la hora actual
        self.label_hora = QLabel(self)
        layout.addWidget(self.label_hora)

        # Crea un QTimer para actualizar periódicamente la hora
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_hora)
        self.timer.start(1000)  # Actualiza cada 1000 milisegundos (1 segundo)

        # Muestra la hora actual inicialmente
        self.actualizar_hora()

    def actualizar_hora(self):
        # Obtiene la hora actual y la muestra en el QLabel
        hora_actual = QTime.currentTime()
        hora_str = hora_actual.toString("hh:mm:ss")
        self.label_hora.setText(hora_str)


if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana()
    ventana.show()
    app.exec_()
