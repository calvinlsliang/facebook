#!/usr/bin/env python
import sys

C = {} # compound list
A = [] # adjacency matrix
M = {} # machine:cost list
V = {} # visited
max_comp = 0
Best = 0

def print_array():
    print
    for i in A:
	print i
    return

def check_array():
    flag = False
    for i in xrange(max_comp):
	for j in xrange(max_comp):
	    a = C.get((i+1, j+1))
	    if a != None:
		if V[C[(i+1, j+1)]] == True:
		    flag = True

	if flag == False:
	    return False
	flag = False

    for i in xrange(max_comp):
	for j in xrange(max_comp):
	    a = C.get((j+1, i+1))
	    if a != None:
	    	if V[C[(j+1, i+1)]] == True:
		    flag = True

	if flag == False:
	    return False
	flag = False

    return True


def dec_array(machine):
    flag = True
    comp1 = machine[1]
    comp2 = machine[2]

    A[comp1-1][comp2-1] += 1

    for i in xrange(max_comp):
        A[comp1-1][i] -= 1
        if A[comp1-1][i] == 0 or not check_array():
	    flag = False
    for i in xrange(max_comp):
        A[i][comp2-1] -= 1
        if A[i][comp2-1] == 0 or not check_array():
	    flag = False

    if flag == False:
	inc_array(machine)

    return flag


def inc_array(machine):
    comp1 = machine[1]
    comp2 = machine[2]
    for i in xrange(max_comp):
        A[comp1-1][i] += 1
    for i in xrange(max_comp):
        A[i][comp2-1] += 1

    A[comp1-1][comp2-1] -= 1
    return

def populate_array():
    for mach in M:
	machine = M[mach]
	comp1 = machine[1]
	comp2 = machine[2]
	for i in xrange(max_comp):
	    A[comp1-1][i] += 1
	for i in xrange(max_comp):
	    A[i][comp2-1] += 1

	A[comp1-1][comp2-1] -= 1
    return

def file_parse(argv):
    f = open(argv, 'r')
    line = (f.readline()).split()
    while line:
	machine = int(line[0][1:])
	comp1 = int(line[1][1:])
	comp2 = int(line[2][1:])
	cost = int(line[3])
	global max_comp
	max_comp = max(comp1, comp2)

	global Best
	Best += cost
	M[machine] = (cost, comp1, comp2)
	V[machine] = True
	C[(comp1, comp2)] = machine
	line = (f.readline()).split()

    for i in xrange(max_comp):
	A.append([])
	for j in xrange(max_comp):
	    A[i].append(0)
    return

def solve():
    max_val = Best
    for m in M:
	for v in V:
	    V[v] = True
	solve_helper(m, max_val)
	print
    print Best
    return

#not correct, outputting only 6*6, not 6! like i want
def solve_helper(machine, cur_value):
    global Best
    V[machine] = False
    #if dec_array(M[machine]) == False:
    print V
    if True == False:
	return
    else:
	cur_value -= M[machine][0] #cost
	if cur_value < Best:
	    Best = cur_value
	for m in M:
	    if V[m] == True:
		solve_helper(m, cur_value)

    V[m] == True
    return

def main():
    file_parse(sys.argv[1])
    populate_array()
    print_array()
    #print check_array()
    solve()
    return

if __name__ == "__main__":
    main()
