#include <iostream>
using namespace std;

int main (){
	int iCasos;
	scanf("%i", &iCasos);
	for(int ix = 0; ix < iCasos; ix ++){
		int iArra[] = {0, 4, 76, 516, 2148, 6768, 17600, 40120, 82608, 157252, 280988};
		int i;
		scanf("%i", &i);
		printf("%i\n", iArra[i]);
	}
}