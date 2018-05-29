#include <iostream>
#include <algorithm>
using namespace std;

int main(){
  char cArra[1010];
  int iN;
  scanf("%i", &iN);
  char uselessChar;
  scanf("%c", &uselessChar);

  for(int i = 0; i < iN; i++){
    char letter;
    scanf("%c", &letter);
    cArra[i] = letter;
  }
  sort(cArra, cArra+iN);

  printf("%c\n", cArra[(iN/2)]);

  return 0;
}