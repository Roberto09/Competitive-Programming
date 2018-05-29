#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct movie{
	vector<int> similarMovies;
	int iVal = 2147483647;
};

int main (){
	int iN, iH, iL;
	scanf("%i %i %i", &iN , &iH , &iL);
	vector<movie> moviesCompareList (iN);
	vector<int> horrorMovies;

	for (int i = 0; i < iH; i++){
		int iHM;
		scanf("%i", &iHM);
		horrorMovies.push_back(iHM);
		moviesCompareList[iHM].iVal = 0;
	}
	for(int i = 0; i < iL; i ++){
		int P1, P2;
		scanf("%i %i", &P1, &P2);
		moviesCompareList[P1].similarMovies.push_back(P2);
		moviesCompareList[P2].similarMovies.push_back(P1);
	}


	for(int i = 0; i < moviesCompareList.size(); i++){
		//cout << "movie id --- " << i <<": {"; 
		for (int iK = 0; iK < moviesCompareList[i].similarMovies.size(); iK ++){
			//cout << moviesCompareList[i].similarMovies[iK] << ", ";
		}
		//cout << endl;
	}









vector<int> forVector = horrorMovies;

	while(forVector.size() != 0){
		//cout << "entre -- parcialmente" << endl;
		vector<int> newForVector;
		for(int i = 0; i < forVector.size(); i++){
			for(int iK = 0; iK < moviesCompareList[forVector[i]].similarMovies.size(); iK++){
				//cout << "id inicial = " << forVector[i] << " > id final = " << moviesCompareList[forVector[i]].similarMovies[iK] << endl; 
				//cout << moviesCompareList[forVector[i]].iVal <<" > " << moviesCompareList[moviesCompareList[forVector[i]].similarMovies[iK]].iVal << endl;
				if(moviesCompareList[forVector[i]].iVal < moviesCompareList[moviesCompareList[forVector[i]].similarMovies[iK]].iVal){
					moviesCompareList[moviesCompareList[forVector[i]].similarMovies[iK]].iVal = moviesCompareList[forVector[i]].iVal + 1;
					//cout << " --------- Entre ------------ " << moviesCompareList[moviesCompareList[forVector[i]].similarMovies[iK]].iVal + 1 << endl;
					if(find(newForVector.begin(), newForVector.end(), moviesCompareList[forVector[i]].similarMovies[iK]) == newForVector.end()){
						newForVector.push_back(moviesCompareList[forVector[i]].similarMovies[iK]);
					}
				}
			}
		}
		forVector = newForVector;
	}

	int iMaxVal = -1;
	int iPos;
	for(int i = 0; i < iN; i++){
		//cout << moviesCompareList[i].iVal << endl;
		if(moviesCompareList[i].iVal > iMaxVal){
			iMaxVal = moviesCompareList[i].iVal;
			iPos = i;
		}
	}

	printf("%i", iPos);

	return 0;
}