import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFormLayout, QWidget, QVBoxLayout, QCalendarWidget, \
    QPushButton


class AppointmentForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulario de Agendamiento de Citas")
        self.setGeometry(100, 100, 400, 300)

        self.initUI()

    def initUI(self):
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        form_layout = QFormLayout()
        main_widget.setLayout(form_layout)

        # Nombre
        lbl_nombre = QLabel("Nombre:")
        form_layout.addRow(lbl_nombre)

        # Apellido
        lbl_apellido = QLabel("Apellido:")
        form_layout.addRow(lbl_apellido)

        # Fecha
        lbl_fecha = QLabel("Fecha:")
        form_layout.addRow(lbl_fecha)

        # Calendario
        calendar_widget = QCalendarWidget()
        form_layout.addRow(calendar_widget)

        # Botón para guardar la cita
        btn_guardar = QPushButton("Guardar Cita")
        form_layout.addRow(btn_guardar)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppointmentForm()
    sys.exit(app.exec_())


