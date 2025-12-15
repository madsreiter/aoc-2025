inputnavn="input12.txt"

with open("../../Input/2025/"+inputnavn) as f:
    inp = []
    for line in f:
        inp.append(line.rstrip())

presents = []
trees = []
p = False
for i in inp:
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

accepted = []
rejected = []
unknown = []
for i, (t, np) in enumerate(trees):
    t_s = t[0] * t[1]
    p_s = sum(a*b for a, b in zip(present_sizes, np))
    if t_s < p_s:
        rejected.append(i)
    elif (t[0]//3) * (t[1]//3) >= sum(np):
        accepted.append(i)
    else:
        unknown.append(i)

if len(unknown):
    print("You're in big trouble mister!")
    print("Answer in interval between " + str(len(accepted)) + " and " + str(len(accepted)+len(unknown)) + ".")
    print(str(len(unknown)) + " christmas with status \"Unknown\" needs further examination.")
else:
    print(len(accepted))

#
#
#
print("Del 2:")
#
#
#

print("Ingen del 2.")