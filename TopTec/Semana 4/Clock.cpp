#include <iostream>
using namespace std;

int main(){

  int iN;
  while(scanf("%i", &iN) != EOF){
    if(iN%6 == 0)
      printf("Y\n");
    else
      printf("N\n");
  }
  return 0;
}
