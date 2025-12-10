inputnavn="input09.txt"

with open("../../Input/2025/"+inputnavn) as f:
    inp = []
    for line in f:
        inp.append(line.rstrip())

inp = [tuple(map(int, i.split(","))) for i in inp]

#
#
#
print("Del 1:")
#
#
#

areas = {}
for ind1 in range(len(inp)):
    tile1 = inp[ind1]
    for ind2 in range(ind1 + 1, len(inp)):
        tile2 = inp[ind2]
        areas[(tile1, tile2)] = (abs(tile1[0]-tile2[0])+1) * (abs(tile1[1]-tile2[1])+1)

areas_sorted = sorted(areas.items(), key=lambda item: item[1], reverse=True)
print(areas_sorted[0][1])
# 4777967538

#
#
#
print("Del 2:")
#
#
#

perimeter_hor = set()
perimeter_ver = set()
tile_gl = inp[-1]
for tile_curr in inp:
    if tile_gl[0] == tile_curr[0]:
        perimeter_hor |= {tuple(sorted([tile_gl, tile_curr]))}
    else:
        perimeter_ver |= {tuple(sorted([tile_gl, tile_curr]))}
    tile_gl = tile_curr


def in_green_fct(s, t):
    row_min = min(s[0], t[0])
    col_min = min(s[1], t[1])
    row_max = max(s[0], t[0])
    col_max = max(s[1], t[1])
    # Left
    if any(e for e in perimeter_hor if row_min < e[0][0] < row_max and e[0][1] <= col_min and e[1][1] >= col_min + 1):
        return False
    # Right
    if any(e for e in perimeter_hor if row_min < e[0][0] < row_max and e[0][1] <= col_max - 1 and e[1][1] >= col_max):
        return False
    # Top
    if any(e for e in perimeter_ver if col_min < e[0][1] < col_max and e[0][0] <= row_min and e[1][0] >= row_min + 1):
        return False
    # Bottom
    if any(e for e in perimeter_ver if col_min < e[0][1] < col_max and e[0][0] <= row_max - 1 and e[1][0] >= row_max):
        return False
    return True


for (t1, t2), a in areas_sorted:
    if in_green_fct(t1, t2):
        print(a)
        break
# 1439894345