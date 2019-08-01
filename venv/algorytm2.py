from liczba import Liczba
from grupy import Grupa
#beda globalne (osobny plik):
N=5
lista_good=[1,2,3,5,7,8]
lista_indiffrent =[19,18,17,0,16]
wyniki = []
zmiana = True
#
def wyswietl(number_list):
    for j in  number_list:
        print(str(j)+": "+str(j.number_binary))
    print("##############")
def dif_of_one_bit(str1, str2):
    rozwiazanie = 0
    c=-1
    for i in range(0, N):
        if str1[i]=="-" and str2[i]!="-":
            return -1
        if (str1[i] == "1" and str2[i] == "0") or (str1[i] == "0" and str2[i] == "1"):
            rozwiazanie += 1
            c=i
        if rozwiazanie > 1:
            return -1
    if c>=0:
        tym=str2[:c]+'-'+str2[c+1:]
        return tym
    return c
def pary(list1, list2):
    if len(list1)<1 or len(list2)<1:
        return True
    else:
        for i in list1:
            for j in list2:
                b=dif_of_one_bit(i.number_binary, j.number_binary)
                if b!=-1:
                    tym=Grupa(b,[i,j])
                    wyniki.append(tym)


def podzial_zal_num_bit(lista):
    j=0
    M = len(lista)
    lista_list=[]
    for k in range(0,N+1):
        listat=[]
        while j<M and k== lista[j].number_of_true_bits:
            listat.append(lista[j])
            j+=1
        lista_list.append(listat)
    return lista_list
def First_loop():
    global wyniki
    lista=[]
    for i in lista_good+lista_indiffrent:
        lista.append(Liczba(int(i)).uzupelnij(N))
    lista = sorted(lista)
    lista = podzial_zal_num_bit(lista)
    for i in range(0,len(lista)-1):
        pary(lista[i],lista[i+1])
    wyswietl(wyniki)
def Next_loop():
    global wyniki, zmiana
    lista = wyniki
    wyniki=[]
    lista = podzial_zal_num_bit(lista)
    for i in range(0, len(lista) - 1):
        pary(lista[i], lista[i + 1])
    if (len(wyniki)==0):
        zmiana=False
    wyswietl(wyniki)

def Algo():
    First_loop()
    while(zmiana):
        Next_loop()
Algo()