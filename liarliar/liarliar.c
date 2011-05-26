#include <stdio.h>

#define LIE 0
#define TRUTH !LIE

typedef struct {
  char *name;
  int liar;
} table;

void flop_liar(char *name, table t[]) {
  table *s;
  
}

int name_exists(char *name, table t[]) {

}

int main(int argc, char* argv[]) {
  FILE *file=fopen(argv[1], "r");
  
  int num=(fgetc(file)-'0');
  printf("%d\n", num);

  table t[num];
  int k;
  for (k=0; k<num; k++) {
    
  }
  
  return 0;
}
