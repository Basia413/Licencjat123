from liczba import Liczba
def wyswietl(number_list):
    for j in  number_list:
        print(j)
    print("##############")
l = [Liczba(13), Liczba(15), Liczba(4), Liczba(3), Liczba(2), Liczba(7)]
for i in l:
    print(i.uzupelnij(4))

wyswietl(l)

def dif_of_one_bit(str1, str2):
    roz = 0
    c=-1
    for i in range(0, len(str1)):
        if str1=="-" and str2!="-":
            return -1
        if (str1[i] == "1" and str2[i] == "0") or (str1[i] == "0" and str2[i] == "1"):
            roz += 1
            c=i
        if roz > 1:
            return -1
    if roz == 1:
        return c
    elif roz == 0:
        return c


def pary(list1, list2):
    if len(list1)<1 or len(list2)<1:
        return []
    else:
        lista = []
        for i in list1:
            for j in list2:
                b=dif_of_one_bit(i.number_binary, j.number_binary)
                if b>=0:
                    lista.append([i, j,b])
        return lista
def podzial_zal_num_bit(lista, N):
    j=0
    M = len(lista)
    lista = sorted(lista)
    lista_list=[]
    for k in range(0,N):
        listat=[]
        while j<M and k== lista[j].number_of_bits:
            listat.append(lista[j])
            j+=1
        lista_list.append(listat)
    return lista_list


def Algorytm(liczby):
    liczby = sorted(liczby)
    N=4+1

    lista_wejsciowa = []
    pary1=[]
    wyswietl(liczby)
    for i in liczby:
        lista_wejsciowa.append(i.number)

    #lista = list(dict.fromkeys(lista))
    podzielone = podzial_zal_num_bit(liczby, N)
    print(len(podzielone))
    for i in range(0,N-1):
        pary1 +=pary(podzielone[i],podzielone[i+1])
    return liczby


#al = Algorytm(l)
