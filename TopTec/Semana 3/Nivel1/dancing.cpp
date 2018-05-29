#include <iostream>
#include <string>

using namespace std;

int main (){
	int iCasos, iParejas;
	scanf("%i",&iCasos);

	for(int i = 0; i < iCasos; i++){
		scanf("%i", &iParejas);
		int iRes = 1;
		for (int i = 1; i <= iParejas; i++){
			iRes = iRes * i;
		}
		printf("Case #%i: %i\n", i+1, iRes);
	}
	return 0;
}