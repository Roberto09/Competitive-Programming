#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

int main (){
	int iArra1[10], iArra2[10], iArraOp[10], iCasos;
	scanf("%i", &iCasos);
	for (int i = 0; i < iCasos; i++){
		scanf("%i", &iArra1[i]);
	}
	for (int i = 0; i < iCasos; i++){
		scanf("%i", &iArra2[i]);
		iArraOp[i] = i;
	}

	//sort(iArra1, iArra1+iCasos);
	//sort(iArra2, iArra2+iCasos);

	int iSumaMenor = INT_MAX;

/*

	for (int i = 0; i < iCasos; i++){
		int iSumaTotal = 0;
		for (int iK = 0; iK < iCasos; iK ++){
			iSumaTotal = iSumaTotal + iArra1[iK] * iArra2[iK]; 
		}
		if (iSumaTotal < iSumaMenor)
			iSumaMenor = iSumaTotal;
	}

*/
//int icont = 0 ;
	do{
		int iSumaTotal = 0;
		for(int i = 0; i < iCasos; i ++){
			//cout << iSumaTotal << " + " << iArra1[i] << " * " << iArra2[i] << endl;
			iSumaTotal = iSumaTotal + iArra1[i] * iArra2[iArraOp[i]];
			}
			//cout << "Suma Total " << iSumaTotal << endl;
			//icont ++;
		if(iSumaTotal < iSumaMenor)
			iSumaMenor = iSumaTotal;
	}while(next_permutation(iArraOp,iArraOp+iCasos));

	printf("%i", iSumaMenor);
	//cout << icont << endl;
}