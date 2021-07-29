#include <stdio.h>

typedef int int7[7];

int7 referenceMat[] = {{1,2,3,4,5,6,7},{1,2,3,4,5,6,7}};

int7* returnPointer()
{
  return referenceMat;
}

int main()  // int main!  not void!
{
  int7* mat;

  mat = returnPointer();
  // do something with the array
  printf("%d\n", mat[0][2]);
  return 0;
}
