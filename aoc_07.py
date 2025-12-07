inputnavn="input07.txt"

with open("../../Input/2025/"+inputnavn) as f:
    inp = []
    for line in f:
        inp.append(line.rstrip())



#
print("Del 1:")
#



del1 = 0
beams = {}
beams[inp[0].index("S")] = 1
for ind in range(1, len(inp)-1):
    prev_beams = beams.copy()
    beams = {}
    for glp in prev_beams:
        if inp[ind][glp] == "^":
            beams[glp-1] = prev_beams[glp] + beams.get(glp-1, 0)
            beams[glp+1] = prev_beams[glp] + beams.get(glp+1, 0)
            del1 += 1
        else:
            beams[glp] = prev_beams[glp] + beams.get(glp, 0)
print(del1)
# 1546



#
print("Del 2:")
#



print(sum(beams.values()))
# 13883459503480