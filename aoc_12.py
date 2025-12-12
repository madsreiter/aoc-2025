inputnavn="input12.txt"

with open("../../Input/2025/"+inputnavn) as f:
    inp = []
    for line in f:
        inp.append(line.rstrip())

presents = []
trees = []
p = False
for x, i in enumerate(inp):
    if ":" in i and len(i) > 2:
        s, n = i.split(": ")
        s = tuple(map(int, s.split("x")))
        n = tuple(map(int, n.split(" ")))
        trees.append((s, n))
    elif ":" in i:
        p = True
        p_t = []
    elif i == "":
        p = False
        presents.append("/".join(p_t))
    elif p:
        p_t.append(i)

#
#
#
print("Del 1:")
#
#
#

present_sizes = [p.count("#") for p in presents]

del1 = 0
for t, np in trees:
    t_s = t[0] * t[1]
    p_s = sum(a*b for a, b in zip(present_sizes, np))
    if p_s <= t_s:
        del1 += 1
print(del1)

#
#
#
print("Del 2:")
#
#
#

print("Ingen del 2.")