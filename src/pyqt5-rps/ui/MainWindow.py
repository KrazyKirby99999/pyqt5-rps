from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

import sys
import os

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "../resources/ui/mainwindow.ui"), self)