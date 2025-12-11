inputnavn="input01.txt"

with open("../../Input/2025/"+inputnavn) as f:
    inp = []
    for line in f:
        inp.append(line.rstrip())

start = 50
modulo = 100



#
print("Del 1:")
#



del1 = 0
del2add = 0
hvor = start
for i in inp:
    retn = 1 if i[0] == "R" else -1
    tal = int(i[1:])
    del2add += int(tal / modulo)
    tal = tal%modulo
    ny_hvor = hvor + retn*tal
    if hvor > 0 > ny_hvor or ny_hvor > modulo:
        del2add += 1
    hvor = ny_hvor % modulo
    if hvor == 0:
        del1 += 1
print(del1)
# 1084



#
print("Del 2:")
#



print(del1+del2add)
# 6475