from number import Number
from groups import Group
import numpy as np
print(2 ** 3)
for i in range(0, 8):
    print(i)
# j = [1, 2, 3, 4, 5, 6, 7, 8]
# print(j[:2], j[2:4])
l = [Number(13), Number(6), Number(4), Number(3), Number(2), Number(7)]
# print(l)
# for i in l:
#     i.fill_with_zeros(4)
# for i in l:
#     print(i)
# for i in sorted(l):
#     print(i)
# # l.fill_with_zeros(6)\
# slowo ="Barbara"
# print(slowo[:2]+"*"+slowo[3:])
# k=str(1010)

s=Group("1--0", [l[1]])
t=Group("11-0", l[3:5])
# s+=t
# k=t.number
print("dugo:",len(s))
t=[[1,3],[2,6]]
print(np.reshape(t, np.size(t)))


