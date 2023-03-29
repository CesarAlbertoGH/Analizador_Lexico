import sys

from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtGui


from vista.home import *
from analizador_lexico import *

class Main(QMainWindow):
    
    def __init__(self):
        
        QMainWindow.__init__(self)

        self.home = Ui_home()
        self.home.setupUi(self)

        # Eventos
        self.home.bt_lexico.clicked.connect(self.ev_lexico)

    def ev_lexico(self):
        '''
        Manejo de analisis de expresion lexemas
        :return: 
        '''
        self.home.tx_lexico.setText('')

        # Obtencion de datos ingresados
        datos = self.home.tx_ingreso.toPlainText().strip()

        # Analisis de los lexemas de los datos ingresados
        resultado_lexico = prueba(datos)

        cadena = ''
        for lex in resultado_lexico:
            cadena += lex + "\n"
        self.home.tx_lexico.setText(cadena)

def iniciar():

    app = QApplication(sys.argv)

    ventana = Main()
 
    ventana.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    iniciar()
