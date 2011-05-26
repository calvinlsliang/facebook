#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	int i;
	float f;
	int n;

	FILE *fin = fopen(argv[1], "r");
	fscanf(fin, "%d", &n);
	printf("%d\n", n);

	char s[n][1024];
	for (i = 0; i < n; i++) {
		fscanf(fin, "%s %f", s[i], &f);
		printf("%s %f %d\n", s[i], f, i);
	}
	
	printf("%s\n", s[0]);
	printf("%s\n", s[1]);
	printf("%s\n", s[2]);
	printf("%s\n", s[3]);

	return 0;
}
