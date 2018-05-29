#include <iostream>
using namespace std;

int main (){
	long long iN = 0;
	long long iSuma = 0;
	long long iValAnt = 0;
	scanf("%lld", &iN);
	for(long long i = 1; i <= iN; i++){
		if(i%2 == 0){
			long long iPar = i;
			while(iPar%2 == 0){
				iPar = iPar/2;
				iValAnt ++;
			}
		}
		iSuma = iSuma + iValAnt;
	}
	printf("%lld", iSuma);
}