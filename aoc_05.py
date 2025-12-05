inputnavn="input05.txt"

with open("../../Input/2025/"+inputnavn) as f:
    inp = []
    for line in f:
        inp.append(line.rstrip())

opdel_data = inp.index("")
inp1 = [list(map(int, i.split("-"))) for i in inp[:opdel_data]]
inp2 = [int(i) for i in inp[opdel_data+1:]]



#
print("Del 1:")
#



tael = 0
for i2 in inp2:
    for i1 in inp1:
        if i1[0] <= i2 <= i1[1]:
            tael += 1
            break
print(tael)
# 661



#
print("Del 2:")
#



def konsolider_int(int_ind):
    int_ind.sort()
    int_ud = []
    int_ud.append(int_ind[0])
    for i1 in int_ind:
        min_i = i1[0]
        max_i = i1[1]
        for r in int_ud:
            if r[0] <= min_i <= r[1]:
                r[1] = max(r[1], max_i)
                break
            elif r[0] <= max_i <= r[1]:
                r[0] = min(r[0], min_i)
                break
        else:
            int_ud.append(i1)
    return int_ud

inp1_k = inp1.copy()
laen = float("Inf")
while len(inp1_k) != laen:
    laen = len(inp1_k)
    inp1_k = konsolider_int(inp1_k)
print(sum([i[1]-i[0]+1 for i in inp1_k]))
# 359526404143208