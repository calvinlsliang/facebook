#!/usr/bin/env python
import sys

# Look at SCC algorithms. Namely Kosaraju, Tarjan, and Gabow. http://en.wikipedia.org/wiki/Strongly_connected_component
C = {} # compound list
M = {} # machine:cost list
V = {} # visited
S = set([]) # set of combinations already visited
Compound_set = set([])
max_comp = 0
Best = 0
Best_combo = ()

def print_list(l):
    for i in l:
	print i,
    print
    return

def print_array(A):
    print
    for i in A:
	print i
    return

def visited_true():
    l = []
    for m in M:
        if V[m] == True:
            l.append(m)
    return tuple((sorted(l)))

def file_parse(argv):
    f = open(argv, 'r')
    line = (f.readline()).split()
    l = []
    global Best_combo
    while line:
	machine = int(line[0][1:])
	comp1 = int(line[1][1:])
	comp2 = int(line[2][1:])
	cost = int(line[3])
	global max_comp
	max_comp = max(comp1, comp2)
	Compound_set.add(comp1)
	Compound_set.add(comp2)

	global Best
	Best += cost
	M[machine] = (cost, comp1, comp2)
	V[machine] = True
	l.append(machine)
	C[(comp1, comp2)] = machine
	line = (f.readline()).split()

    Best_combo = sorted(l)
    return

def make_empty_arr():
    A = []
    for i in xrange(max_comp):
	A.append([])
	for j in xrange(max_comp):
	    A[i].append(float('inf'))
    return A

def algorithm():
    return floyd_warshall()

def floyd_warshall():
    ea = make_empty_arr()

    for m in M:
	if V[m] == True:
	    comp1 = M[m][1]
	    comp2 = M[m][2]
	    cost = M[m][0]
	    ea[comp1-1][comp2-1] = cost

    for k in Compound_set:
	for i in Compound_set:
	    for j in Compound_set:
		if i != j:
		    if ea[i-1][k-1] + ea[k-1][j-1] < ea[i-1][j-1]:
			ea[i-1][j-1] = ea[i-1][k-1] + ea[k-1][j-1]

    for i in Compound_set:
	for j in Compound_set:
	    if i != j:
		if ea[i-1][j-1] == float('inf'):
		    return False
    return True

def solve(val):
    for m in M:
	solve_helper(m, val)
    return

def solve_helper(machine, cur_value):
    global Best
    global Best_combo
    V[machine] = False
    vt = visited_true()
    if vt not in S:
        S.add(vt)
	if algorithm() == True:
            cur_value -= M[machine][0]
            if cur_value < Best:
                Best = cur_value
		Best_combo = list(vt)
	    for m in M:
		if V[m] == True:
		    solve_helper(m, cur_value)
    V[machine] = True
    return

def main():
    file_parse(sys.argv[1])
    #solve_helper(1, Best)
    solve(Best)
    print Best
    print_list(Best_combo)

    return

if __name__ == "__main__":
    main()
