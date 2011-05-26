#!/usr/bin/env python
import sys
import time

G = {} # adjacency list
N = {} # next list
V = {} # visited list
P = {} # probability list
Nodes = set()
Start = None
Best = float('inf')
#Time = 0

def file_parse():
    f = open(sys.argv[1], 'r')
    num_prob = f.readline()
    if num_prob == "":
	print "%.2f" % float(-1.00)
	sys.exit()
    num_prob = int(num_prob)
    for i in range(num_prob):
	loc = (f.readline()).split()
	P[loc[0]] = float(loc[1])
	Nodes.add(loc[0])
	V[loc[0]] = False
	if i == 0:
	    global Start
	    Start = loc[0] 

    for i in Nodes:
	for j in Nodes:
	    if i == j: G[(i, j)] = 0
	    else: G[(i, j)] = float('inf')
	    N[(i, j)] = None

    num_nodes = f.readline()
    if num_nodes == "":
	print "%.2f" % float(-1.00)
	sys.exit()
    num_nodes = int(num_nodes)
    for i in range(num_nodes):
	loc = (f.readline()).split()
	G[(loc[0], loc[1])] = float(loc[2])
	G[(loc[1], loc[0])] = float(loc[2])

def floyd_warshall():
    for k in Nodes:
	for i in Nodes:
	    for j in Nodes:
		if G[(i, k)] + G[(k, j)] < G[(i, j)]:
		    G[(i, j)] = G[(i, k)] + G[(k, j)]
		    N[(i, j)] = k
		    N[(j, i)] = k
    return

def double_check():
    for a in Nodes:
	for b in Nodes:
	    if G[(a, b)] == float('inf'):
		print "%.2f" % float(-1.00)
		sys.exit()
    return

Counter = 0
def find_best_path(cur_loc, cur_dist, exp_val):
    global Best
    global Counter
    V[cur_loc] = True
    exp_val += P[cur_loc]*cur_dist

    at_end = True
    for a in Nodes:
	if V[a] == False:
	    at_end = False
	    if (exp_val+P[a]*(cur_dist+G[(cur_loc, a)])) < Best:
		'''
		'''
		Counter += 1
		print a, '%d ' % Counter, exp_val, cur_dist, Best
		'''
		'''

		find_best_path(a, cur_dist+G[(cur_loc, a)], exp_val)

    if at_end:
	if exp_val < Best:
	    Best = exp_val

    V[cur_loc] = False
    return

def initialize_first_best():
    exp_val = 0
    cur_dist = 0

    sorted_prob = sorted(P, reverse=True)
    sorted_prob.remove(Start)
    a = Start
    for b in sorted_prob:
	cur_dist += G[(a, b)]
	exp_val += cur_dist*P[b]
	a = b
    Best = exp_val
    return




def main():
    #global Time

    #Time = time.time()
    file_parse()
    #print "Parse:", time.time()-Time

    #Time = time.time()
    floyd_warshall()
    #print "Floyd-Warshall:", time.time()-Time

    #Time = time.time()
    double_check()
    #print "Double check:", time.time()-Time

    initialize_first_best()

    #Time = time.time()
    find_best_path(Start, 0, 0)
    #print "Best path:", time.time()-Time

    print "%.2f" % Best

    return

if __name__ == "__main__":
    main()
