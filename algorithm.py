from number import Number
from groups import Group
from PyQt5.QtWidgets import *
import variables
import itertools as it

change = True
#Funkcja do testowania
def wyswietl(number_list):
    for j in number_list:
        print(str(j) + ": " + str(j.number_binary))
    print("##############")


def dif_of_one_bit(str1, str2):
    result = 0
    c = -1
    for i in range(0, variables.N):
        if str1[i] == "-" and str2[i] != "-":
            return -1
        if (str1[i] == "1" and str2[i] == "0") or (str1[i] == "0" and str2[i] == "1"):
            result += 1
            c = i
        if result > 1:
            return -1
    if c >= 0:
        tym = str2[:c] + '-' + str2[c + 1:]
        return tym
    return c


def pairs(list1, list2):
    if len(list1) < 1 or len(list2) < 1:
        return True
    else:
        for i in list1:
            for j in list2:
                b = dif_of_one_bit(i.number_binary, j.number_binary)
                if b != -1:
                    i.used()
                    j.used()
                    tym = Group(b, [i.number, j.number])
                    variables.results.append(tym)


def division_dep_am_bits(lista):
    j = 0
    M = len(lista)
    lista_list = []
    for k in range(0, variables.N + 1):
        listat = []
        while j < M and k == lista[j].number_of_true_bits:
            listat.append(lista[j])
            j += 1
        lista_list.append(listat)
    return lista_list


def First_loop():
    lista = []
    list_copy = []
    for i in variables.lista_good + variables.lista_indiffrent:
        lista.append(Number(int(i)).fill_with_zeros(variables.N))
    lista = sorted(lista)
    for i in lista:
        list_copy.append(str(i)+":"+str(i.number_binary))
    lista = division_dep_am_bits(lista)
    for i in range(0, len(lista) - 1):
        pairs(lista[i], lista[i + 1])
    not_used(lista)
    wyswietl(variables.results)
    # l_end = list(dict.fromkeys(l_end))
    return list_copy, variables.results


def Next_loop():
    global change
    lista = variables.results
    variables.results = []
    lista = division_dep_am_bits(lista)
    for i in range(0, len(lista) - 1):
        pairs(lista[i], lista[i + 1])
    if (len(variables.results) == 0):
        change = False
    wyswietl(variables.results)
    not_used(lista)
    return variables.results

def not_used(lista):
    for j in lista:
        for i in j:
            if i.use == False:
                variables.l_end.append(i)

def result_combination():
    flag = True
    i=1
    while(flag and i<=len(variables.l_end)):
        if i == 1:
            for j in variables.l_end:
                if mach([j]):
                    flag = False
                    variables.solutions.append([j])
        else:
            combination = list(it.combinations(variables.l_end, i))
            for j in combination:
                if mach(j):
                    flag = False
                    variables.solutions.append(j)

        i+=1
    print("rozwizania:")
    for k in variables.solutions:
        wyswietl(k)


def mach(comb):
    tym_list = variables.lista_good.copy()
    for i in comb:
        if type(i.number) is int:
            if i.number in tym_list:
                tym_list.remove(i.number)
        else:
            for j in i.number:
                if j in tym_list:
                    tym_list.remove(j)
    if len(tym_list)>0:
        return False
    else:
        return True



def Algo():
    global change
    list_of_results = []
    tym1,tym2 =First_loop()
    list_of_results.append(tym1)
    list_of_results.append(tym2)
    while (change):
        tym =Next_loop()
        list_of_results.append(tym)
    variables.l_end = list(dict.fromkeys(variables.l_end))
    wyswietl(variables.l_end)
    result_combination()
    return list_of_results
Algo()