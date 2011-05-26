#include <string>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <map>
#include <queue>
using namespace std;

// Author: Calvin Liang <cliang4@berkeley.edu>

int main(int argc, char* argv[]) {
    if (argc != 2) {
	cout << "Incorrect number of arguments." << endl;
	exit(0);
    }

    ifstream in;
    in.open(argv[1]);
    string s;

    // The first line is the number of unique members
    getline(in, s);
    int members = atoi(s.c_str());

    /*
    ** map dict: a map of string:member_name to int:index
    ** bool mat[][]: an adjacency matrix of who accused who
    ** bool visited[]: a boolean array of whether the member has been 
    **     traversed or not
    */ 
    map <string, int> dict;
    bool mat[members][members];
    bool visited[members];

    // Initalize the matrix and arrays to false
    for (int i = 0; i < members; i++) {
	visited[i] = false;
	for (int j = 0; j < members; j++) {
	    mat[i][j] = false;
	}
    }

    string accuser;
    string accusee;
    int num_accused;
    int member_index = 0;

    /* 
    ** Iterates over the number of unique members and sets true to the
    ** accuser and accusee at its appropriate matrix index.
    **
    ** If the user doesn't exist in the map, add it in with an increasing
    ** unique index counter.
    */
    for (int i = 0; i < members; i++) {
	in >> accuser;
	if (dict.find(accuser) == dict.end()) { 
	    dict[accuser] = member_index;
	    member_index++;
	}

	in >> s;
	num_accused = atoi(s.c_str());

	for (int j = 0; j < num_accused; j++) {
	    in >> accusee;
	    if (dict.find(accusee) == dict.end()) { 
		dict[accusee] = member_index;
		member_index++;
	    }
	    mat[dict[accuser]][dict[accusee]] = true;
	    mat[dict[accusee]][dict[accuser]] = true;
	}
    }

    /*
    ** A check to make sure the matrix is fine and dandy, since
    ** I can't create a helper function to do it since 
    ** you have to pass in bounds for all dimensions except the first.
    */
    /*
    cout << "Printing adjacency matrix..." << endl;
    for (int i = 0; i < members; i++) {
	for (int j = 0; j < members; j++) {
	    cout << mat[i][j] << " ";
	}
	cout << endl;
    }
    cout << endl;
    */

    queue<int> q;
    bool color = true;
    int c1 = 0;
    int c2 = 0;
    int row = 0;

    /*
    ** A quick BFS implementation, alternating between "colors" (0 or 1)
    ** when all of the children of a particular parent are traversed.
    **
    ** -1 signifies all the children have been traversed, and a color swap
    ** is needed.
    */

    q.push(0);
    q.push(-1);
    while (!q.empty()) {
	//cout << q.front() << endl;
	row = q.front();
	q.pop();
	if (row == -1) {
	    color = !color;
	    if (q.empty()) {
		break;
	    }
	    q.push(-1);
	} else if (visited[row] == false) {
	    if (color) {
		c1++;
	    } else {
		c2++;
	    }
	    visited[row] = true;
	    for (int j = 0; j < members; j++) {
		if (mat[row][j]) {
		    q.push(j);
		}
	    }
	}
    }

    cout << max(c1, c2) << " " << min(c1, c2) << endl;

    return 0;
}
