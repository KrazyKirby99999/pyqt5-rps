from PyQt5.QtWidgets import QAction, QMainWindow
from PyQt5 import uic

import sys
import os
import random

from data.matches import result

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "../resources/ui/mainwindow.ui"), self)

        self.game_reset()
        
    def game_reset(self):
        buttons = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5, self.pushButton_6]

        for button in buttons:
            try:
                button.disconnect()
            except:
                pass

        self.label_3.setText("P1's Choice?")
        self.turn = 1
        self.human = None
        self.p1_move = "rock"
        self.p2_move = random.choice(["rock","paper","scissors"])
        self.result = None

        self.connect_page0()
        self.connect_page1()
        self.connect_page2()

        self.stackedWidget.setCurrentIndex(0)

    def connect_page0(self):
        def human_button_pressed():
            self.stackedWidget.setCurrentIndex(1)
            self.human = 1
        self.pushButton.clicked.connect(human_button_pressed)
        
        def computer_button_pressed():
            self.stackedWidget.setCurrentIndex(1)
            self.human = 0
        self.pushButton_2.clicked.connect(computer_button_pressed)
    
    def connect_page1(self):
        def rock_button_pressed():
            if self.turn == 1:
                self.p1_move = "rock"
                self.label_3.setText("P2's Choice?")
                if not self.human: computer_turn()
            if self.turn == 2:
                self.p2_move = "rock"
                self.stackedWidget.setCurrentIndex(2)
            self.turn = 2
            self.set_page2_labels()
        self.pushButton_3.clicked.connect(rock_button_pressed)

        def paper_button_pressed():
            if self.turn == 1:
                self.p1_move = "paper"
                self.label_3.setText("P2's Choice?")
                if not self.human: computer_turn()
            if self.turn == 2:
                self.p2_move = "paper"
                self.stackedWidget.setCurrentIndex(2)
            self.turn = 2
            self.set_page2_labels()
        self.pushButton_4.clicked.connect(paper_button_pressed)

        def scissors_button_pressed():
            if self.turn == 1:
                self.p1_move = "scissors"
                self.label_3.setText("P2's Choice?")
                if not self.human: computer_turn()
            if self.turn == 2:
                self.p2_move = "scissors"
                self.stackedWidget.setCurrentIndex(2)
            self.turn = 2
            self.set_page2_labels()
        self.pushButton_5.clicked.connect(scissors_button_pressed)

        def computer_turn():
            self.stackedWidget.setCurrentIndex(2)
    
    def connect_page2(self):
        def play_again_button_pressed():
            self.game_reset()
        self.pushButton_6.clicked.connect(play_again_button_pressed)
        self.set_page2_labels()
    
    def set_page2_labels(self):
        self.label_5.setText("P1 chose " + self.p1_move)
        self.label_6.setText("P2 chose " + self.p2_move)
        if result(self.p1_move,self.p2_move) == 'p1':
            self.label_4.setText("P1 won!")
        if result(self.p1_move,self.p2_move) == 'p2':
            self.label_4.setText("P2 won!")
        if result(self.p1_move,self.p2_move) == 'draw':
            self.label_4.setText("Draw")

        
