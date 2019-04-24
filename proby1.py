from liczba import Liczba

print(2 ** 3)
for i in range(0, 8):
    print(i)
j = [1, 2, 3, 4, 5, 6, 7, 8]
print(j[:2], j[2:4])
l = [Liczba(13), Liczba(6), Liczba(4), Liczba(3), Liczba(2), Liczba(7)]
print(l)
for i in l:
    i.uzupelnij(4)
for i in l:
    print(i)
for i in sorted(l):
    print(i)
# l.uzupelnij(6)
