#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import zmienne
import algorytm
import grupy

# N = zmienne.N


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = 'Minimalizacja Quine\'a - McCluskey\'a'
        self.left = 10
        self.top = 30
        self.width = 640
        self.height = 480
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.flag = False
        self.flag2 = False
        #Layout
        self.Stack = QStackedWidget()
        self.uklad = QWidget()
        self.uklad.setLayout(self.uklad1())
        self.Stack.addWidget(self.uklad)
        self.setCentralWidget(self.Stack)
        # self.Stack.addWidget(selfuklad2())
        # self.Stack.setCurrentIndex(1)
        # self.Stack.setLayout(self.uklad1())
        # # self.setLayout(self.Stack)
        # self.c_widget = QWidget()
        # self.c_widget.addWidget(self.Stack)
        # self.setCentralWidget(self.c_widget)
        # self.Stack.setCurrentIndex(0)
        # self.setLayout(self.uklad)
        # self.show()
        #self.initUI()
        # self.Stack.show()


    # def initUI(self):
    #     self.setWindowTitle(self.title)
    #     self.setGeometry(self.left, self.top, self.width, self.height)
    #### Ukad 1
    def uklad1(self):
        uklad = QFormLayout()
        self.napis = QLabel("Podaj liczbe bitow wejsciowych", self)
        self.Pb = QPushButton("Dalej")
        self.Sb = QSpinBox()
        self.Sb.setRange(1, 12)
        uklad.addWidget(self.napis)
        uklad.addWidget(self.Sb)
        uklad.addWidget(self.Pb)
        self.Pb.clicked.connect(self.btn1_cliked)
        return uklad

    def btn1_cliked(self):
        zmienne.N = self.Sb.value()
        print(zmienne.N)
        print(self.flag2)
        print("Dump: {}".format(self.Stack.dumpObjectInfo()))
        if self.flag2:
            pass

        uklad = QWidget()
        uklad.setLayout(self.uklad2())
        self.Stack.addWidget(uklad)
        self.Stack.setCurrentIndex(1)

    ### Uklad 2
    def uklad2(self):
        uklad = QVBoxLayout()
        uklad.addLayout(self.funkcja_n())
        uklad.addLayout(self.radio_b())
        print("Ukad 2", zmienne.N)
        uklad.addLayout(self.chose_num())
        uklad.addLayout(self.menu())
        self.good.clicked.connect(lambda: self.flag_true())
        self.inddif.clicked.connect(lambda: self.flag_false())
        self.b1.clicked.connect(lambda: self.Stack.setCurrentIndex(0))
        self.b2.clicked.connect(lambda: self.saveN())
        self.b3.clicked.connect(lambda: self.solving())
        return uklad

    def funkcja_n(self):
        u = QHBoxLayout()
        nap1 = QLabel("f( x,y,z) = sum(", self)
        nap2 = QLabel(") + sum_n(")
        nap3 = QLabel(")")
        self.Le1 = QLineEdit()
        self.Le2 = QLineEdit()
        u.addWidget(nap1)
        u.addWidget(self.Le1)
        u.addWidget(nap2)
        u.addWidget(self.Le2)
        u.addWidget(nap3)
        return u

    def radio_b(self):
        self.good = QRadioButton("Pozytywne")
        self.inddif = QRadioButton("Obojetne")
        u2 = QHBoxLayout()
        u2.addStretch()
        u2.addWidget(self.good)
        u2.addWidget(self.inddif)
        u2.addStretch()
        return u2

    def chose_num(self):
        self.flag2=True
        u = QGridLayout()
        print("Chosse num", zmienne.N)
        self.tab1 = []
        for i in range(0, 2 ** zmienne.N):
            self.tab1.append(QCheckBox(str(i)))
        j = 0
        leng = len(self.tab1)
        rang = (2 ** zmienne.N) // 3 + 1
        print(leng)

        for i in range(0, 3):
            for k in range(0, rang):
                if j >= leng: break
                u.addWidget(self.tab1[j], k, i)
                j += 1
        return u

    def menu(self):
        u = QHBoxLayout()
        self.b1 = QPushButton("Cofnij")
        self.b2 = QPushButton("Zapisz")
        self.b3 = QPushButton("Rozwiaz")
        u.addWidget(self.b1)
        u.addWidget(self.b2)
        u.addWidget(self.b3)
        return u


    def flag_true(self):
        # self.saveN()
        self.flag = True
        self.radio_changed()

    def flag_false(self):
        # self.saveN()
        self.flag = False
        self.radio_changed()

    def radio_changed(self):
        for i in range(0, 2 ** zmienne.N):
            self.tab1[i].setChecked(False)
            if not self.flag:
                if i in zmienne.lista_indiffrent:
                    self.tab1[i].setChecked(True)
            else:
                if i in zmienne.lista_good:
                    self.tab1[i].setChecked(True)

    def saveN(self):
        label = ""
        if self.flag:
            zmienne.lista_good.clear()
            for i in range(0, 2**zmienne.N):
                if self.tab1[i].isChecked():
                    zmienne.lista_good.append(i)
                    zmienne.lista_good = list(dict.fromkeys(zmienne.lista_good))
            for i in zmienne.lista_good:
                label += str(i) + ", "
            label = label[:len(label) - 2]
            self.Le1.setText(label)
        else:
            zmienne.lista_indiffrent.clear()
            for i in range(0, 2 ** zmienne.N):
                if self.tab1[i].isChecked():
                    zmienne.lista_indiffrent.append(i)
                    zmienne.lista_indiffrent = list(dict.fromkeys(zmienne.lista_indiffrent))
            for i in zmienne.lista_indiffrent:
                label += str(i) + ", "
            label = label[:len(label) - 2]
            self.Le2.setText(label)
    def solving(self):
        self.lista_wynikow = algorytm.Algo()
        algorytm.wyswietl(zmienne.l_end)
        uklad = QWidget()
        uklad.setLayout(self.uklad3())
        self.Stack.addWidget(uklad)
        self.Stack.setCurrentIndex(2)
    #### uklad 3
    def uklad3(self):
        uklad = QFormLayout()
        # uklad.alignment()
        self.l = QLabel("Hurra to tabelka wywala", self)
        text=''
        for j in self.lista_wynikow:
            tym = ''
            for k in j:
                tym += str(k) + "\n"
            uklad.addWidget(QLabel(tym[:len(tym)-1], self))
        for i in zmienne.l_end:
            text +=str(i) + "\n"
        self.tab_print = QLabel(text[:len(text)-1],self)
        uklad.addWidget(self.tab_print)
        return uklad


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('windowsvista')
print(QStyleFactory.keys())
ex = App()
ex.show()
sys.exit(app.exec_())
