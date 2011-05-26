/* 
   Author: Calvin Liang
   E-mail: cliang4@berkeley.edu
   Phone Number: (408) 600-9781
*/
#include <stdio.h>
#include <string.h>

void hoppity(int i) {
  if (i%3==0 && i%5==0) {
    printf("Hop\n");
  } else if (i%3==0) {
    printf("Hoppity\n");
  } else if (i%5==0) {
    printf("Hophop\n");
  }
  return;
}

int main(int argc, char* argv[]) {
  if (argc==1) exit(1);
  FILE *file;
  file=fopen(argv[1], "r");

  char c;
  int k, i=0;

  c=fgetc(file);
  while (c==' ') c=fgetc(file);
  while (c>='0' && c<='9') {
    i*=10;
    i+=(c-'0');
    c=fgetc(file);
  }

  for (k=1; k<=i; k++) {
    hoppity(k);
  }
  return 0;
}
