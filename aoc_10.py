from itertools import combinations
from scipy.optimize import milp

inputnavn="input10.txt"

with open("../../Input/2025/"+inputnavn) as f:
    inp = []
    for line in f:
        inp.append(line.rstrip())

inp = [
        (
        sum({2**i for i, x in enumerate(ld[1:-1]) if x=="#"}),
        [set(map(int, b[1:-1].split(','))) for b in bws],
        tuple(map(int, jr[1:-1].split(',')))
        )
        for ld, *bws, jr in map(lambda x: x.split(" "), inp)
         ]


def xor_fct(liste):
    #return reduce(lambda i, j: i ^ j, liste)
    res = 0
    for l in liste:
        res ^= l
    return res


#
#
#
print("Del 1:")
#
#
#

p1 = 0
for ld, bws, _ in inp:
    bbws = {sum({2 ** x for x in bb}) for bb in bws}
    for n_tryk in range(1, len(bbws)+1):
        if any(i for i in combinations(bbws, n_tryk) if xor_fct(i) == ld):
            p1 += n_tryk
            break
    else:
        raise ValueError("Fejl. Ingen løsning fundet for ld=" + str(ld) + " og bws=" + str(bbws) + ".")
print(p1)
# 434

#
#
#
print("Del 2:")
#
#
#

p2 = 0
for _, bws, jr in inp:
    c = [1] * len(bws)
    # Optimering vha. lineær optimering over integers
    # Matricen A er givet ved:
    # A[i, j] = (i in bws[j]) for i=0,...,len(jr), j=0,...,len(bws).
    A = [[i in b for b in bws] for i in range(len(jr))]
    p2 += round(milp(c, integrality=1, constraints=[A, jr, jr]).fun)
print(p2)
# 15132