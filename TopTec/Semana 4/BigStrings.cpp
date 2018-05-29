#include <iostream>
#include <string.h>
using namespace std;

int main(){
  int iOperators;
  scanf("%i", &iOperators);
  int iSuma = 0;
  int Multiplicacion = 1;

  //Strings
  char sOperando[1];

  for(int i = 0; i < iOperators; i++){
  	char sN[10];
  	scanf("%s", &sN);
    //Obtener Valor String Numeral
    int iValorTotal = 0;
      for(int iC = 0; iC < strlen(sN); iC ++){
        int iValorChar;
        if(sN[iC] == '.')
          iValorChar = 1;
        else if(sN[iC] == '-')
          iValorChar = 5;
        else if(sN[iC] == ':')
          iValorChar = 2;
        else
          iValorChar = 10;
      iValorTotal = iValorTotal + iValorChar;
      }
      
      //Decidir que hacer de acuerdo a operando
      scanf("%s", &sOperando);
      cout << sOperando << endl;
      if(sOperando == "+"){
     	iSuma = iSuma + iValorTotal*Multiplicacion;
        Multiplicacion = 1;
      }
      else{
      	cout << "multiplicacion" << endl;
        Multiplicacion = Multiplicacion*iValorTotal;
      }
  }


  cout << iSuma << endl;
  	char sN[10];
    scanf("%s", &sN);
    //Obtener Valor String Numeral
    int iValorTotalLastN = 0;
      for(int iC = 0; iC < strlen(sN); iC ++){
        int iValorChar;
        if(sN[iC] == '.')
          iValorChar = 1;
        else if(sN[iC] == '-')
          iValorChar = 5;
        else if(sN[iC] == ':')
          iValorChar = 2;
        else
          iValorChar = 10;
      iValorTotalLastN = iValorTotalLastN + iValorChar;
      }
      
      iSuma = iSuma + iValorTotalLastN*Multiplicacion;
      printf("%i\n", iSuma);
  
  return 0;
}