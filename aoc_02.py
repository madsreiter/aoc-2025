inputnavn="input02.txt"

with open("../../Input/2025/"+inputnavn) as f:
    inp = []
    for line in f:
        inp.append(line.rstrip())

inp = inp[0].split(",")

def ceildiv_fct(a, b):
    return -(a // -b)



#
print("Del 1:")
#



del1 = 0
for i in inp:
    suml = []
    tal = i.split("-")
    tal0 = len(tal[0]) // 2
    if tal0 == 0:
        nedre = 1
    else:
        nedre = int(tal[0][:tal0])
    tal1 = ceildiv_fct(len(tal[1]), 2)
    for t in range(nedre, int(tal[1][:tal1])+1):
        tt = int(str(t)+str(t))
        if int(tal[0]) <= tt <= int(tal[1]):
            suml.append(tt)
    del1 += sum(set(suml))
print(del1)
# 18893502033



#
print("Del 2:")
#



suml = []
for i in inp:
    tal = i.split("-")
    len0 = len(tal[0])
    len1 = len(tal[1])
    for n_cifre in range(1,(len1//2)+1):
        for tal_del in range(10**(n_cifre-1), 10**n_cifre):
            for gentag in range(len0//n_cifre, (len1//n_cifre)+1):
                if gentag >= 2:
                    tal_sammensat = int(str(tal_del)*gentag)
                    if tal_sammensat in range(int(tal[0]), int(tal[1])+1):
                        suml.append(tal_sammensat)
print(sum(set(suml)))
# 26202168557