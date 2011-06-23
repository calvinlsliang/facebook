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
    def __init__(self, m, c1, c2):
	self.machine = m
        self.comp1 = c1
        self.comp2 = c2
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
	Compound_set.add(Node(machine, comp1, comp2))

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
    return tarjan()
    #return floyd_warshall()

def floyd_warshall():
    ea = make_empty_arr()

    for m in M:
	if V[m] == True:
	    comp1 = M[m][1]
	    comp2 = M[m][2]
	    cost = M[m][0]
	    ea[comp1-1][comp2-1] = cost

    for k in xrange(max_comp):
        for i in xrange(max_comp):
            for j in xrange(max_comp):
		if i != j:
		    if ea[i][k] + ea[k][j] < ea[i][j]:
                        ea[i][j] = ea[i][k] + ea[k][j]

    for i in xrange(max_comp):
        for j in xrange(max_comp):
	    if i != j:
		if ea[i][j] == float('inf'):
		    return False
    return True

def tarjan():
    index = 0
    global Sets
    ea = make_empty_arr()

    node = None

    for m in M:
	if V[m] == True:
	    comp1 = M[m][1]
	    comp2 = M[m][2]
	    cost = M[m][0]
            node = Node(m, comp1, comp2)
	    ea[comp1-1][comp2-1] = node

    if node == None:
        return False

    tarjan_helper(node, ea, index)


    global SCC
    if len(SCC) == 1:
        if len(SCC[0]) == 1:
            SCC = []
            Sets = set([])
            return False
        elif len(Sets) == max_comp:
            SCC = []
            Sets = set([])
            return True
        else:
            SCC = []
            Sets = set([])
            return False
    else:
        SCC = []
        Sets = set([])
        return False

Sets = set([])
def tarjan_helper(node, adj_list, index):
    global SCC
    global Stack
    node.index = index
    node.lowlink = index
    index += 1
    Stack.append(node)
    Sets.add(node.machine)
    for i in xrange(max_comp):
        if adj_list[node.comp1-1][i] != float('inf'):
            n = adj_list[node.comp1-1][i]
            if n.index == -1:
                tarjan_helper(n, adj_list, index)
                node.lowlink = min(node.lowlink, n.lowlink)
            else:
                for i in xrange(len(Stack)):
                    if Stack[i] == n:
                        node.lowlink = min(node.lowlink, n.index)

    if node.lowlink == node.index:
        comp = []
        n = Stack.pop()
        comp.append(n)
        while (n != node):
            n = Stack.pop()
            comp.append(n)
        SCC.append(comp)
    return

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
    print Best, Counter
    print_list(Best_combo)

    return

if __name__ == "__main__":
    main()
