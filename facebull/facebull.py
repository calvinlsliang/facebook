#!/usr/bin/env python
import sys

C = {} # compound list
A = [] # adjacency matrix
M = {} # machine:cost list
max_comp = 0

def print_array(arr):
    print
    for i in arr:
	print i

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

	M[machine] = (cost, comp1, comp2)
	C[(comp1, comp2)] = machine
	line = (f.readline()).split()

    for i in xrange(max_comp):
	A.append([])
	for j in xrange(max_comp):
	    A[i].append(0)

def main():
    file_parse(sys.argv[1])
    populate_array()

if __name__ == "__main__":
    main()
