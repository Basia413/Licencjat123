#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFormLayout, QPushButton, QSpinBox


class App(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'Minimalizacja Quine\'a - McCluskey\'a'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        uklad = QFormLayout()
        # napis =QLabel("Podaj liczbe bitow wejsciowych", self)
        #         #
        #         # Pb = QPushButton("Dalej")
        #         # Sb = QSpinBox()
        #         # Sb.setRange(1,20)
        #         # uklad.addWidget(napis)
        #         # uklad.addWidget(Sb)
        #         # uklad.addWidget(Pb)
        #         # self.setLayout(uklad)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
