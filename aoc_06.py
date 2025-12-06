import math

inputnavn="input06.txt"

with open("../../Input/2025/"+inputnavn) as f:
    inp = []
    for line in f:
        #inp.append(line.rstrip())
        inp.append(line)

inp_operator = inp[-1].split()
inp.pop()


def sum_prod(tal_liste, oper_liste):
    res = 0
    for ind in range(len(tal_liste)):
        res += sum(tal_liste[ind]) if oper_liste[ind] == "+" else math.prod(tal_liste[ind])
    return res



#
print("Del 1:")
#



inp1a = [i.split() for i in inp]
l_inp1a = len(inp1a)

inp1b = []
for c in range(len(inp1a[0])):
    t_inp = []
    for r in range(l_inp1a):
        t_inp.append(int(inp1a[r][c]))
    inp1b.append(t_inp)

print(sum_prod(inp1b, inp_operator))
# 4405895212738



#
print("Del 2:")
#



inp2a = [i.replace("\n", "") for i in inp]

inp2b = []
temp = []
for c in range(len(inp2a[0])):
    t = ""
    for r in range(len(inp2a)):
        t += inp2a[r][c]
    if t.replace(" ", "") == str():
        inp2b.append(temp)
        temp = []
    else:
        temp.append(int(t))
inp2b.append(temp)

print(sum_prod(inp2b, inp_operator))
# 7450962489289