from liczba import Liczba
from grupy import Grupa
import numpy as np
print(2 ** 3)
for i in range(0, 8):
    print(i)
# j = [1, 2, 3, 4, 5, 6, 7, 8]
# print(j[:2], j[2:4])
l = [Liczba(13), Liczba(6), Liczba(4), Liczba(3), Liczba(2), Liczba(7)]
# print(l)
# for i in l:
#     i.uzupelnij(4)
# for i in l:
#     print(i)
# for i in sorted(l):
#     print(i)
# # l.uzupelnij(6)\
# slowo ="Barbara"
# print(slowo[:2]+"*"+slowo[3:])
# k=str(1010)

s=Grupa("11-0",[l[1]])
t=Grupa("11_0", l[3:5])
# s+=t
# k=t.number
t=[[1,3],[2,6]]
print(np.reshape(t, np.size(t)))

