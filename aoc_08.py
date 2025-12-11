from math import prod
import time

inputnavn="input08.txt"

with open("../../Input/2025/"+inputnavn) as f:
    inp = []
    for line in f:
        inp.append(line.rstrip())

inp = [list(map(int, i.split(","))) for i in inp]

N_connections = 1000

# Squareroot i snot used in dist to preserve integers, as only ordering is needed.
def dist_fct(l1, l2):
    #return sum([(i1-i2)**2 for i1, i2 in zip(l1, l2)])**0.5
    return sum([(i1 - i2) ** 2 for i1, i2 in zip(l1, l2)])

N_junctions = len(inp)

#
#
#
print("Del 1:")
#
#
#

t0 = time.time()

# Find which connections to make
min_dists = [float("Inf")] * N_connections
min_dist_junctions = [None] * N_connections
for j1 in range(N_junctions):
    for j2 in range(j1):
        curr_d = dist_fct(inp[j1], inp[j2])
        if curr_d < min_dists[-1]:
            min_dists = sorted(min_dists[:-1] + [curr_d])
            curr_i = min_dists.index(curr_d)
            min_dist_junctions = min_dist_junctions[:curr_i] + [(j1, j2)] + min_dist_junctions[curr_i:-1]

# Make connections
circuits = [[i] for i in range(N_junctions)]
for curr in min_dist_junctions:
    inder = []
    for ind in range(2):
        for ind_g in range(len(circuits)):
            if curr[ind] in circuits[ind_g]:
                inder.append(ind_g)
    if len(set(inder)) > 1:
        circuits[inder[0]] += circuits[inder[1]]
        circuits.pop(inder[1])

# Find the product of the size of the 3 biggest circuits
print(prod(sorted([len(g) for g in circuits], reverse=True)[:3]))
# 81536
print("Tid del 1 =", time.time()-t0)

#
#
#
print("Del 2:")
#
#
#

t0 = time.time()

d_dist = {}
for j1 in range(N_junctions):
    for j2 in range(j1):
        d_dist[(j2, j1)] = dist_fct(inp[j1], inp[j2])

def circuits_fct(dict_dist, remove=True, max_times=None, debug_print=False):
    # Set circuit numbers
    d_circuits = {}
    for i in range(N_junctions):
        d_circuits[i] = i

    iter = 0
    n_grp = len(set(d_circuits.values()))
    while n_grp > 1:
        iter += 1
        if debug_print and (n_grp % 50 == 0):
            print(n_grp)

        # Find minimum-distance (to connect)
        min_dist = min(dict_dist.values())
        # Find indices of minimum distance junctions. (Indices are there names in this code)
        ind_junctions = [j for j, v in dict_dist.items() if v == min_dist][0]
        # Find indices of circuits of minimum distance junctions
        ind_circuits = sorted([d_circuits[i] for i in ind_junctions])

        # Remove minimum distance from dict_dist
        # If remove=True, also remove all distances between now connected circuits
        circuit1 = [j for j, v in d_circuits.items() if v == d_circuits[ind_circuits[1]]]
        if remove:
            circuit0 = [j for j, v in d_circuits.items() if v == d_circuits[ind_circuits[0]]]
            for c0 in circuit0:
                for c1 in circuit1:
                    dict_dist.pop((min(c0,c1), max(c0,c1)))
        else:
            dict_dist.pop(tuple(ind_junctions))

        # Update circuit number for junctions in circuit1
        d_circuits.update(dict(zip(circuit1, (d_circuits[ind_circuits[0]],)*len(circuit1))))

        if iter == max_times:
            circuitnumbers = [g for g in d_circuits.values()]
            return prod(sorted([circuitnumbers.count(x) for x in set(circuitnumbers)], reverse=True)[:3])

        n_grp = len(set(d_circuits.values()))
    return inp[ind_junctions[0]][0] * inp[ind_junctions[1]][0]


#print("Del1 =", circuits_fct(d_dist.copy(), remove=False, max_times=N_connections))
print("Del2 =", circuits_fct(d_dist.copy()))
# 7017750530
print("Tid del 2 =", time.time()-t0)