#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
#include <limits.h>
#include <sstream>
using namespace std;

/*
** Author: Calvin Liang <cliang4@berkeley.edu>
** An example of a dynamic programming problem: edit distance
** Solved using Levenshtein distance, using pseudo-code from:
**    http://en.wikipedia.org/wiki/Levenshtein_distance
*/

#define FLAG 0

void a(int a) {
    if (FLAG) {
	cout << "=====" << a << endl;
	cout.flush();
    }
    return;
}

string upper_to_lower(string s) {
    char str[s.length()];
    strcpy(str, s.c_str());
    for (int i = 0; i < s.length(); i++) {
	str[i] += ' ';
    }
    return string(str);
}

int minimum(int a, int b, int c) {
    return min(a, min(b, c));
}

int levenshtein_distance(string s, string t) {
    int len_s = s.length();
    int len_t = t.length();

    a(6);

    int d[len_s+1][len_t+1];

    for (int i = 0; i <= len_s; i++) {
	for (int j = 0; j <= len_t; j++) {
	    d[i][j] = 10000;
	}
    }

    for (int i = 0; i <= len_s; i++) {
	d[i][0] = i;
    }
a(7);

    for (int i = 0; i <= len_t; i++) {
	d[0][i] = i;
    }

    a(8);

    for (int j = 1; j <= len_t; j++) {
	for (int i = 1; i <= len_s; i++) {
	    if (s[i-1] == t[j-1]) {
		d[i][j] = d[i-1][j-1];
	    } else {
		d[i][j] = minimum(
		    d[i-1][j] + 1,
		    d[i][j-1] + 1,
		    d[i-1][j-1] + 1
		    );
	    }
	}
    }

    /*
    cout << "Printing adjmatrix..." << endl;
    for (int i = 0; i <= len_s; i++) {
	for (int j = 0; j <= len_t; j++) {
	    cout << d[i][j] << " ";
	}
	cout << endl;
    }
    */

    return d[len_s][len_t];
}

int min_in_dict(vector<string> *d, string s) {

    a(4);
    vector<string>::iterator itr;
    int mini = 1000;
    string word;
    for (itr = d->begin(); itr != d->end(); itr++) {
	a(6);
	if (itr->length() < s.length()+2) {
	    word = upper_to_lower(*itr);
	    mini = min(mini, levenshtein_distance(s, word));
	}
    }

    a(5);
    return mini;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
	cout << "Incorrect number of arguments." << endl;
	exit(0);
    }

    a(0);

    ifstream in(argv[1]);
    //ifstream in_dict("twl06.txt");
    ifstream in_dict("/var/tmp/twl06.txt");
    string s;
    string word;
    vector<string> dict;

    a(1);

    while (in_dict.good()) {
	getline(in_dict, s);
	//s = upper_to_lower(s);
	if (s[s.length()-1] == 0x0D) {
	    s = s.substr(0, s.length()-1);
	}
	dict.push_back(s);
    }
    
    a(2);

    int counter = 0;

    while (in >> word) {
	counter += min_in_dict(&dict, word);
	//cout << word << " " << counter << endl;
    }

    cout << counter << endl;

    return 0;
}
