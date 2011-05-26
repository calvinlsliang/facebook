#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define GRAPHSIZE 2048
#define MAXSIZE 1024
#define INFINITY GRAPHSIZE*GRAPHSIZE
#define MAX(a, b) ((a > b) ? (a) : (b))

int edges; /* The number of nonzero edges in the graph */
int nodes; /* The number of nodes in the graph */
long dist[GRAPHSIZE][GRAPHSIZE]; /* dist[i][j] is the distance between node i and j; or 0 if there is no direct connection */
long d[GRAPHSIZE]; /* d[i] is the length of the shortest path between the source (s) and node i */
int prev[GRAPHSIZE]; /* prev[i] is the node that comes right before i in the shortest path from the source to i*/

/* returns the index of if string t exists in the char array s */
int find(char **s, int size, char *t) {
	int i;
	for (i = 0; i < size; i++) {
		if (strcmp(s[i], t) == 0) {
			return i;
		}
	}
	return -1;
}

void printD() {
	int i;

	printf("Distances:\n");
	for (i = 0; i < nodes; i++)
		printf("%10d", i);
	printf("\n");
	for (i = 0; i < nodes; i++) {
		printf("%10ld", d[i]);
	}
	printf("\n");
}

/*
 * Prints the shortest path from the source to dest.
 *
 * dijkstra(int) MUST be run at least once BEFORE
 * this is called
 */
void printPath(int dest) {
	if (prev[dest] != -1)
		printPath(prev[dest]);
	printf("%d ", dest);
}

void dijkstra(int s) {
	int i, k, mini;
	int visited[GRAPHSIZE];

	for (i = 0; i < nodes; i++) {
		d[i] = INFINITY;
		prev[i] = -1; /* no path has yet been found to i */
		visited[i] = 0; /* the i-th element has not yet been visited */
	}

	d[s] = 0;

	for (k = 0; k < nodes; k++) {
		mini = -1;
		for (i = 0; i < nodes; i++)
			if (!visited[i] && ((mini == -1) || (d[i] < d[mini])))
				mini = i;

		visited[mini] = 1;

		for (i = 0; i < nodes; i++)
			if (dist[mini][i])
				if (d[mini] + dist[mini][i] < d[i]) {
					d[i] = d[mini] + dist[mini][i];
					prev[i] = mini;
				}
	}
}

int main(int argc, char *argv[]) {
	int i, j;
	int  v, w, x;
	float f;

	// change "input" to "argv[1]" later
	FILE *fin = fopen("input", "r");
	fscanf(fin, "%d", &nodes);

	char *s[nodes];
	char t[MAXSIZE];
	char u[MAXSIZE];

	for (i = 0; i < nodes; i++) {
		s[i] = malloc(MAXSIZE);
		fscanf(fin, "%s %f", s[i], &f);
	}

	fscanf(fin, "%d", &edges);

	for (i = 0; i < edges; ++i)
		for (j = 0; j < edges; ++j)
			dist[i][j] = 0;
	for (i = 0; i < edges; ++i) {
		fscanf(fin, "%s%s%d", t, u, &x);
		v = find(s, nodes, t);
		w = find(s, nodes, u);
		printf("%d %d %d\n", v, w, x);
		dist[v][w] = x;
	}
	fclose(fin);
	//dijkstra(0);
	dijkstra(1);
	//dijkstra(2);
	//dijkstra(3);

	printD();

	printf("\n");
	for (i = 0; i < nodes; i++) {
		printf("Path to %d: ", i);
		printPath(i);
		printf("\n");
	}

	return 0;
}
