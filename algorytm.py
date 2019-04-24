from liczba import Liczba

l = [Liczba(13), Liczba(6), Liczba(4), Liczba(3), Liczba(2), Liczba(7)]
for i in l:
    i.uzupelnij(4)
    print(i)


def dif_of_one_bit(str1, str2):
    roz = 0
    for i in range(0, len(str1)):
        if (str1[i] == "1" and str2[i] == "0") or (str1[i] == "0" and str2[i] == "1"):
            roz += 1
        if roz > 1:
            return False
    if roz == 1:
        return True
    elif roz == 0:
        return False


def pary(list1, list2):
    lista = []
    for i in list1:
        for j in list2:
            if dif_of_one_bit(i.number_binary, j.number_binary):
                lista.append([i.number, j.number])
    return lista


def Algorytm(liczby):
    liczby = sorted(liczby)

    # pary_l = pary(liczby[:2], liczby[2:4])
    return liczby


al = Algorytm(l)
