from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

from ui.MainWindow import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()