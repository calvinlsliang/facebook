import sys
import time

A = {} #temp adj list
G = {} #full adjacency list
N = {} #next list
V = {} #visited list
P = {} #probability list
Nodes = set()
Start = None
Best = float('inf')

def file_parse(argv1):
    f = open(argv1, 'r')
    num_prob = int(f.readline())
    for i in range(num_prob):
	loc = (f.readline()).split()
	P[loc[0]] = float(loc[1])
	if i == 0:
	    global Start
	    Start = loc[0] 
    num_nodes = int(f.readline())
    for i in range(num_nodes):
	loc = (f.readline()).split()
	Nodes.add(loc[0])
	Nodes.add(loc[1])
	V[loc[0]] = False
	V[loc[1]] = False
	A[(loc[0], loc[1])] = int(loc[2])
	A[(loc[1], loc[0])] = int(loc[2])

    for i in Nodes:
	for j in Nodes:
	    if i == j: G[(i, j)] = 0
	    else: G[(i, j)] = float('inf')
	    N[(i, j)] = None

    for i in A:
	G[i] = A[i]

def floyd_warshall():
    for k in Nodes:
	for i in Nodes:
	    for j in Nodes:
		if G[(i, k)] + G[(k, j)] < G[(i, j)]:
		    G[(i, j)] = G[(i, k)] + G[(k, j)]
		    N[(i, j)] = k
		    N[(j, i)] = k
    return

def get_path(i, j):
    a = flatten((i, path(i, j), j))
    for i in range(a.count(None)):
	a.remove(None)
    return a

def path(i, j):
    if G[(i, j)] == float('inf'):
	return -1.00
    k = N[(i, j)]
    if k == None:
	return 
    else:
	return path(i, k), k, path(k, j)

# http://kogs-www.informatik.uni-hamburg.de/~meine/python_tricks
def flatten(x):
    result = []
    for el in x:
	#if isinstance(el, (list, tuple)):
	if hasattr(el, "__iter__") and not isinstance(el, basestring):
	    result.extend(flatten(el))
	else:
	    result.append(el)
    return result

def double_check():
    for a in Nodes:
	for b in Nodes:
	    if G[(a, b)] == float('inf'):
		c = float(-1.00)
		print "%.2f" % c
		sys.exit()
    return

def find_best_path(cur_loc, cur_dist, exp_val):
    global Best
    V[cur_loc] = True
    exp_val += P[cur_loc]*cur_dist

    at_end = True
    for a in Nodes:
	if not V[a]:
	    at_end = False
	    if exp_val < Best:
		find_best_path(a, cur_dist+G[(cur_loc, a)], exp_val)

    if at_end:
	if exp_val < Best:
	    Best = exp_val

    V[cur_loc] = False
    return

def main():
    t = time.time()
    file_parse(sys.argv[1])
    floyd_warshall()
    double_check()
    find_best_path(Start, 0, 0)
    print "%.2f" % Best

    return

if __name__ == "__main__":
    main()
