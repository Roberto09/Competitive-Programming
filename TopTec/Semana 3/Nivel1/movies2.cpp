#include <iostream>
#include <vector>
using namespace std;

struct movie{
	vector<int> similarMovies;
	int iVal = 1000;
};

int main (){
	int iN, iH, iL;
	scanf("%i %i %i", &iN , &iH , &iL);
	vector<movie> moviesCompareList (iN);
	vector<bool> horrorMoviesMap(iN, false);

	int ilen = 0;

	for (int i = 0; i < iH; i++){
		int iHM;
		scanf("%i", &iHM);
		horrorMoviesMap[iHM] = true;
		ilen ++;
		moviesCompareList[iHM].iVal = 0;
	}
	for(int i = 0; i < iL; i ++){
		int P1, P2;
		scanf("%i %i", &P1, &P2);
		moviesCompareList[P1].similarMovies.push_back(P2);
		//moviesCompareList[P2].similarMovies.push_back(P1);
	}

vector<bool> forVector = horrorMoviesMap;

	while(ilen != 0){
		vector<bool> newForVector(iN, false);
		int newLen = 0;
		for(int i = 0; i < iN; i++){
			if(forVector[i]){
				for(int iK = 0; iK < moviesCompareList[i].similarMovies.size(); iK++){
					if(moviesCompareList[i].iVal < moviesCompareList[moviesCompareList[i].similarMovies[iK]].iVal){
						moviesCompareList[moviesCompareList[i].similarMovies[iK]].iVal = moviesCompareList[i].iVal + 1;
						if(!newForVector[moviesCompareList[i].similarMovies[iK]]){
							newForVector[moviesCompareList[i].similarMovies[iK]] = true;
							newLen ++;
						}
					}
					else if(moviesCompareList[i].iVal > moviesCompareList[moviesCompareList[i].similarMovies[iK]].iVal){
						moviesCompareList[i].iVal = moviesCompareList[moviesCompareList[i].similarMovies[iK]].iVal + 1;
					}
				}
			}
		}
		forVector = newForVector;
		ilen = newLen;
	}

	int iMaxVal = -1;
	int iPos;
	for(int i = 0; i < iN; i++){
		//cout << moviesCompareList[i].iVal <<endl;
		if(moviesCompareList[i].iVal > iMaxVal){
			iMaxVal = moviesCompareList[i].iVal;
			iPos = i;
		}
	}

	printf("%i", iPos);

	return 0;
}