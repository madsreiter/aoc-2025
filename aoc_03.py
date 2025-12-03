inputnavn="input03.txt"

with open("../../Input/2025/"+inputnavn) as f:
    inp = []
    for line in f:
        inp.append(line.rstrip())

n_cifre_1 = 2
n_cifre_2 = 12

def battery_fkt(n_cifre):
    res = 0
    for i in inp:
        cifre = []
        for ciffer in range(n_cifre):
            ciffer = max([t for t in i[:len(i)-n_cifre+ciffer+1]])
            ciffer_ind = i.index(ciffer)
            i = i[ciffer_ind+1:]
            cifre.append(ciffer)
        res += int("".join(cifre))
    return res



#
print("Del 1:")
#



# del1 = 0
# for i in inp:
#     ciffer1 = max([t for t in i[:len(i)-1]])
#     maks_ind = i.index(ciffer1)
#     ciffer2 = max([t for t in i[maks_ind+1:]])
#     del1 += int(ciffer1+ciffer2)
# print(del1)

print(battery_fkt(n_cifre_1))
# 17524



#
print("Del 2:")
#



print(battery_fkt(n_cifre_2))
# 173848577117276