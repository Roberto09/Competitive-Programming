#include <iostream>
#include <vector>
using namespace std;

int main(){
  int iN = -1;
  vector <int> resultados;
  vector <int> numeros;
  int iMayor = -1;
  while(iN != 0){
    scanf("%i", &iN);
    if(iN > iMayor){
      iMayor = iN;
    }
    numeros.push_back(iN);
  }

  int suma = 1;
  int iValor = 1;
  resultados.push_back(1);
  for(int i = 1; i <= iMayor; i ++){
    iValor = (iValor * 2) % 1000000007;
    suma = (suma + iValor)% 1000000007;
    resultados.push_back(suma);
  }
  int len = numeros.size()-1;
  for(int i = 0; i < len; i ++){
    printf("%i\n", resultados[numeros[i]]);
  }

}