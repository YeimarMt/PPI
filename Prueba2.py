import sys

from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QAction, QHBoxLayout, QFormLayout, QWidget, QSizePolicy, QSpacerItem, QLineEdit, \
    QDateTimeEdit, QComboBox, QApplication, QMainWindow


class ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.nombre_ventana = "valorizador"
        self.initUI()
        self.resize(640, 480)

    def initUI(self):
        self.setWindowTitle(self.nombre_ventana)
        menu=self.menuBar()
        archivo=menu.addMenu("Archivo")
        boton_guardar=QAction("Guardar",self)

        widget = QWidget(self)
        self.setCentralWidget(widget)
        flay = QFormLayout()



        cal = QDateTimeEdit(self)
        cal.setCalendarPopup(True)
        cal.setDisplayFormat("dd-MM-yyyy")
        cal.calendarWidget().setLocale(QLocale(QLocale.Spanish))


        flay.addRow("Fecha vencimiento", cal)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ventana()
    ex.show()
    sys.exit(app.exec_())