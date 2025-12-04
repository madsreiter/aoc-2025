inputnavn="input04.txt"

with open("../../Input/2025/"+inputnavn) as f:
    inp = []
    for line in f:
        inp.append(line.rstrip())

R = len(inp)
C = len(inp[0])

d = {}
for r in range(R):
    for c in range(C):
        d[(r,c)] = 1 if inp[r][c] == "@" else 0

org_sum = sum(d.values())

naboer = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]



#
print("Del 1:")
#



res = 0
for r in range(R):
    for c in range(C):
        if d[(r,c)] == 1:
            adjacent = 0
            for n in naboer:
                nr = r + n[0]
                nc = c + n[1]
                if (nr, nc) in d:
                    adjacent += d[(nr,nc)]
            #print(r,c,adjacent)
            if adjacent < 4:
                res += 1
print(res)
# 1460



#
print("Del 2:")
#



gl_sum = R*C
iter = 0
while sum(d.values()) != gl_sum:
    iter += 1
    gl_sum = sum(d.values())
    for r in range(R):
        for c in range(C):
            if d[(r, c)] == 1:
                adjacent = 0
                for n in naboer:
                    nr = r + n[0]
                    nc = c + n[1]
                    if (nr, nc) in d:
                        adjacent += d[(nr, nc)]
                if adjacent < 4:
                    d[(r,c)] = 0
print(org_sum-sum(d.values()))
# 9243