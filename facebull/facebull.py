#!/usr/bin/env python
import sys

# Look at SCC algorithms. Namely Kosaraju, Tarjan, and Gabow. http://en.wikipedia.org/wiki/Strongly_connected_component
C = {} # compound list
M = {} # machine:cost list
V = {} # visited
S = set([]) # set of combinations already visited
Stack = []
SCC = []
Compound_set = set([])
max_comp = 0
Best = 0
Best_combo = ()

class Node:
    def __init__(self, m):
	self.machine = m
	self.index = -1
	self.lowlink = -1

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
	Compound_set.add(Node(comp1))
	Compound_set.add(Node(comp2))

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

def algorithm(machine):
    return tarjan(machine)
    #return floyd_warshall()

def floyd_warshall():
    ea = make_empty_arr()

    for m in M:
	if V[m] == True:
	    comp1 = M[m][1]
	    comp2 = M[m][2]
	    cost = M[m][0]
	    ea[comp1-1][comp2-1] = cost

    for knode in Compound_set:
	for inode in Compound_set:
	    for jnode in Compound_set:
		k = knode.machine
		i = inode.machine
		j = jnode.machine
		if i != j:
		    if ea[i-1][k-1] + ea[k-1][j-1] < ea[i-1][j-1]:
			ea[i-1][j-1] = ea[i-1][k-1] + ea[k-1][j-1]

    for inode in Compound_set:
	for jnode in Compound_set:
	    i = inode.machine
	    j = jnode.machine
	    if i != j:
		if ea[i-1][j-1] == float('inf'):
		    return False
    return True

def tarjan(node):
    index = 0
    ea = make_empty_arr()

    for m in M:
	if V[m] == True:
	    comp1 = M[m][1]
	    comp2 = M[m][2]
	    cost = M[m][0]
	    ea[comp1-1][comp2-1] = cost

    tarjan_helper(node, ea, index)


    # clean node values, reset them all to -1
    return len(SCC)

def tarjan_helper(node, adj_list, index):
    pass





def solve(val):
    for m in M:
	solve_helper(m, val)
    return

Counter = 0
def solve_helper(machine, cur_value):
    global Best
    global Best_combo
    global Counter
    V[machine] = False
    vt = visited_true()
    if vt not in S:
	Counter += 1
        S.add(vt)
	if algorithm(next(iter(vt))) == True:
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
    print Best, Counter
    print_list(Best_combo)

    return

if __name__ == "__main__":
    main()
