#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import variables
import algorithm


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
        self.str_variables = ""
        # Layout
        self.Stack = QStackedWidget()
        self.arrangement = QWidget()
        self.arrangement.setLayout(self.arragement1())
        self.Stack.addWidget(self.arrangement)
        self.setCentralWidget(self.Stack)

    def print_variables(self):
        for i in range(97, 97 + variables.N):
            self.str_variables += chr(i) + ", "
        self.str_variables = self.str_variables[:len(self.str_variables) - 2]

    #### Uklad 1
    def arragement1(self):
        uklad = QFormLayout()
        self.napis = QLabel("Podaj liczbę bitów wejściowych: ", self)
        self.Pb = QPushButton("Dalej")
        self.Sb = QSpinBox()
        self.Sb.setRange(1, 12)
        uklad.addWidget(self.napis)
        uklad.addWidget(self.Sb)
        uklad.addWidget(self.Pb)
        self.Pb.clicked.connect(self.btn1_cliked)
        return uklad

    def btn1_cliked(self):
        variables.N = self.Sb.value()
        self.print_variables()
        uklad = QWidget()
        uklad.setLayout(self.arragement2())
        self.Stack.addWidget(uklad)
        self.Stack.setCurrentIndex(1)

    ### Uklad 2
    def arragement2(self):
        arraggement = QVBoxLayout()
        arraggement.addLayout(self.funcion_n())
        arraggement.addLayout(self.radio_b())

        Sa = QScrollArea()
        Sa.setWidget(self.chose_num())
        Sa.setWidgetResizable(True)
        Sa.setFixedHeight(400)
        arraggement.addWidget(Sa)
        arraggement.addLayout(self.menu())

        self.good.clicked.connect(lambda: self.flag_true())
        self.inddif.clicked.connect(lambda: self.flag_false())
        self.b2.clicked.connect(lambda: self.saveN())
        self.b3.clicked.connect(lambda: self.solving())
        return arraggement

    def funcion_n(self):
        u = QHBoxLayout()
        nap1 = QLabel("f(" + self.str_variables + ") =∑(", self)
        nap2 = QLabel(") + ∑n(")
        nap3 = QLabel(")")
        self.Le1 = QLabel()
        self.Le2 = QLabel()
        u.addWidget(nap1)
        u.addWidget(self.Le1)
        u.addWidget(nap2)
        u.addWidget(self.Le2)
        u.addWidget(nap3)
        return u

    def radio_b(self):
        self.lb3 = QLabel("Wybierz opcje: ")
        self.good = QRadioButton("Pozytywne")
        self.inddif = QRadioButton("Obojętne")
        u2 = QHBoxLayout()
        u2.addStretch()
        u2.addWidget(self.lb3)
        u2.addWidget(self.good)
        u2.addWidget(self.inddif)
        u2.addStretch()
        return u2

    def chose_num(self):
        Gb = QGroupBox("Wybierz liczby (Przed zmianą opcji naciśnij zapisz)")
        u = QGridLayout()
        self.tab1 = []
        for i in range(0, 2 ** variables.N):
            self.tab1.append(QCheckBox(str(i)))
        j = 0
        leng = len(self.tab1)
        rang = (2 ** variables.N) // 3 + 1

        for i in range(0, 3):
            for k in range(0, rang):
                if j >= leng: break
                u.addWidget(self.tab1[j], k, i)
                j += 1
        Gb.setLayout(u)
        return Gb

    def menu(self):
        u = QHBoxLayout()
        # self.b1 = QPushButton("Cofnij")
        self.b2 = QPushButton("Zapisz")
        self.b3 = QPushButton("Rozwiąż")
        # u.addWidget(self.b1)
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
        for i in range(0, 2 ** variables.N):
            self.tab1[i].setChecked(False)
            if not self.flag:
                if i in variables.lista_indiffrent:
                    self.tab1[i].setChecked(True)
            else:
                if i in variables.lista_good:
                    self.tab1[i].setChecked(True)

    def saveN(self):
        label = ""
        if self.flag:
            variables.lista_good.clear()
            for i in range(0, 2 ** variables.N):
                if self.tab1[i].isChecked():
                    variables.lista_good.append(i)
                    variables.lista_good = list(dict.fromkeys(variables.lista_good))
            for i in variables.lista_good:
                label += str(i) + ", "
            label = label[:len(label) - 2]
            self.Le1.setText(label)
        else:
            variables.lista_indiffrent.clear()
            for i in range(0, 2 ** variables.N):
                if self.tab1[i].isChecked():
                    variables.lista_indiffrent.append(i)
                    variables.lista_indiffrent = list(dict.fromkeys(variables.lista_indiffrent))
            for i in variables.lista_indiffrent:
                label += str(i) + ", "
            label = label[:len(label) - 2]
            self.Le2.setText(label)

    def solving(self):
        uklad = QWidget()
        try:
            self.lista_wynikow = algorithm.Algo()

        except:
            pass
        uklad.setLayout(self.arragment3())
        self.Stack.addWidget(uklad)
        self.Stack.setCurrentIndex(2)

    #### Uklad 3
    def arragment3(self):
        u = QVBoxLayout()
        self.l1 = QLabel("Tabele:", self)
        self.l2 = QLabel("Rozwiązanie: ")
        u.addWidget(self.l1)
        Sa = QScrollArea()
        Sa.setWidget(self.tables())
        Sa.setWidgetResizable(True)
        Sa.setFixedHeight(400)
        u.addWidget(Sa)
        u.addWidget(self.l2)
        u.addLayout(self.solution())
        self.bt = QPushButton("Zakończ")
        u.addWidget(self.bt)
        self.bt.clicked.connect(lambda: sys.exit())
        return u

    def tables(self):
        uklad = QHBoxLayout()
        text = ''
        for j in self.lista_wynikow:
            tym = ''
            if len(j) > 0:
                for k in j:
                    tym += str(k) + "\n------------\n"
                tab1 = QLabel(tym[:len(tym) - 1], self)  # ,c,r)
                tab1.setAlignment(Qt.AlignRight)
                uklad.addWidget(tab1)
                uklad.addStretch(20)
        for i in variables.l_end:
            text += str(i) + "\n------------\n "
        self.tab_print = QLabel(text[:len(text) - 1], self)
        self.tab_print.setAlignment(Qt.AlignRight)
        uklad.addWidget(self.tab_print)
        uklad.addStretch(20)
        Gb = QGroupBox()
        Gb.setLayout(uklad)
        return Gb

    def solution(self):
        uklad = QFormLayout()
        tym = ""
        for i in variables.solutions:
            tym += "f(" + self.str_variables + ")= "
            for j in i:
                tym += self.char_group(j.number_binary) + " + "
            else:
                if len(i)==1 and  len(i[0])==0:
                    tym = tym[:len(tym) - 3]
                    tym += str(1) + "   "
            tym = tym[:len(tym) - 3] + "\n\n"
        text = QLabel(tym)
        uklad.addWidget(text)
        return uklad

    def char_group(self, str1):
        text = ""
        character = 97
        for i in range(0, variables.N):
            if str1[i] == "-":
                pass
            elif str1[i] == "1":
                text += chr(character)
            elif str1[i] == "0":
                text += "~" + chr(character)
            character += 1
        return text

    def arragment3_err(self):
        u = QFormLayout()
        self.l1e = QLabel("Nie Wprowadziłeś żadnej wartości!")
        self.bt2 = QPushButton("Zakoncz")
        u.addWidget(self.l1e)
        u.addWidget(self.bt2)
        self.bt2.clicked.connect(lambda: sys.exit())
        return u


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('windowsvista')
ex = App()
ex.show()
sys.exit(app.exec_())
