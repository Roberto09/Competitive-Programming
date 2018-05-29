#include <iostream>
#include <math.h>  
using namespace std;

int main (){
	int iNum, iRes = 0;
	scanf("%i", &iNum);
	do{
		iNum = iNum/2;
		iRes ++;
	}while(iNum != 0);
	printf("%i", iRes);
	return 0;
}