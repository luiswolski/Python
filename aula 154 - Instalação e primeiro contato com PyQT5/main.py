import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

# Criando os atributos de estilo do botãp
        self.btn = QPushButton('Texto do Botão')
        self.btn.setStyleSheet('font-size: 30px')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        self.btn.clicked.connect(lambda: print('Hello word!'))

        self.setCentralWidget(self.cw)      # Inicializando o botão


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
