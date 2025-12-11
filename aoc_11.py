inputnavn="input11.txt"

with open("../../Input/2025/"+inputnavn) as f:
    inp = []
    for line in f:
        inp.append(line.rstrip())

start1 = "you"
finish = "out"

start2 = "svr"
target1 = "dac"
target2 = "fft"

devices = { i.split(": ")[0]: set(i.split(": ")[1].split(" ")) for i in inp}


def path_fct(curr, end, dic):
    if curr == end:
        return 1
    elif curr == "out":
        return 0
    if curr not in dic:
        dic[curr] = sum(path_fct(til, end, dic) for til in devices[curr])
    return dic[curr]


#
#
#
print("Del 1:")
#
#
#

print(path_fct(start1, finish, dic={}))
# 699

#
#
#
print("Del 2:")
#
#
#

t1t2 = path_fct(target1, target2, dic={})
if t1t2 > 0:
    foerst = path_fct(start2, target1, dic={})
    mellem = t1t2
    sidst = path_fct(target2, finish, dic={})
else:
    foerst = path_fct(start2, target2, dic={})
    mellem = path_fct(target2, target1, dic={})
    sidst = path_fct(target1, finish, dic={})
print(foerst * mellem * sidst)
# 388893655378800

# Løsning til del 1 inden generalisering til del 2:

# del1 = 0
# positions = [start1]
# while len(positions) > 0:
#     curr = positions.pop()
#     if curr == finish:
#         del1 += 1
#         continue
#     positions.extend(list(devices[curr]))
# print(del1)