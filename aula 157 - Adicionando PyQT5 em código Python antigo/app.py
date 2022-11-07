import sys
from geracpf import gera_cpf
from validacfp import valida_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow
import qdarkstyle
import design


class GeraValidaCPF(QMainWindow ,design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
        self.btnGeraCPF.clicked.connect(self.gera_cpf)
        self.btnValidaCPF.clicked.connect(self.valida_cpf)

    def gera_cpf(self):
        self.labelRetorno.setStyleSheet("color: white")
        self.labelRetorno.setText(
            str(gera_cpf())
        )

    def valida_cpf(self):
        cpf = self.inputValidaCPF.text()
        test = valida_cpf(cpf)

        if test is True:
            self.labelRetorno.setStyleSheet("color: green")
            self.labelRetorno.setText(
                'CPF Verdadeiro'
            )
        else:
            self.labelRetorno.setStyleSheet("color: red")
            self.labelRetorno.setText(
                'CPF Falso!'
            )



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeraValidaCPF()
    gera_valida_cpf.show()
    qt.exec_()
