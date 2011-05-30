#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <limits.h>
#include <map>
using namespace std;

/*
* Author: Calvin Liang <cliang4@berkeley.edu>
*
* Finding Sophie is TSP with probability attached.
* Solved using the Floyd-Warshall algorithm with a basic backtracking pruning
* technique.
*
* Already implemented using Python (about 12 seconds for 17 nodes), but I wanted
* to implement in C++ for practice and speed increase. Plus I'll be making my
* data structures more efficient.
*/

/*
* index: the position in the nodes array a particular location lies. 
*     The first index is designated as the starting location.
* prob: the probability that Sophie will be at a location
* visited: if the location has been visited or not. Initialized to false.
*/
struct Node {
    int index;
    double prob;
    bool visited;
    Node() {
	index = 0;
	prob = 1.0;
	visited = false;
    }
    Node(int i, double p) {
	index = i;
	prob = p;
	visited = false;
    }
};

/*
* Global variables
*
* Best: the current best solution time
* nodes: array of Nodes
* dists: adjacency matrix of places and distances
* dict: hash of place:index position
* num_places: the number of different locations Sophie can hide
*/

double Best = ULONG_MAX;
Node **nodes;
double **dists;
map <string, int> dict;
int num_places;

void parse_file(char *s) {
    ifstream in(s);
    string str;
    double d;

    // Reads first line to find out how many locations Sophie could be hiding at
    in >> num_places;
    //num_places = strtod(s);

    // Allocate space for Nodes array and adjacency matrix
    nodes = new Node*[num_places];
    dists = new double*[num_places];
    for (int i = 0; i < num_places; i++) {
	dists[i] = new double[num_places];
	for (int j = 0; j < num_places; j++) {
	    dists[i][j] = ULONG_MAX;
	}
    }

    // For each line, update the nodes array and dictionary
    //Node n;
    for (int i = 0; i < num_places; i++) {
	in >> str;
	in >> d;
	dict[str] = i;
	nodes[i] = new Node(i, d);
    }

    // Reads the next line to find out how many unique distances there are
    in >> d;
    string location1;
    string location2;
    double distance;
    for (int i = 0; i < d; i++) {
	in >> location1;
	in >> location2;
	in >> distance;

	dists[dict[location1]][dict[location2]] = distance;	
	dists[dict[location2]][dict[location1]] = distance;	
    }

    in.close();
    return;
}

void print_everything() {
    cout << "Best: " << Best << endl;
    cout << "num_places: " << num_places << endl;
    cout << "Printing node list..." << endl;
    Node *n;
    for (int i = 0; i < num_places; i++) {
	n = nodes[i];
	cout << n->index << " " << n->prob << " " << n->visited << endl;
    }

    cout << "\nPrinting dists list..." << endl;
    for (int i = 0; i < num_places; i++) {
	for (int j = 0; j < num_places; j++) {
	    cout << dists[i][j] << " ";
	}
	cout << endl;
    }
}




int main(int argc, char* argv[]) {
    parse_file(argv[1]);
    //floyd_warshall();
    //find_best_path(0, 1, 0);
    //printf("%.2f\n", Best);

    print_everything();

    return 0;
}
