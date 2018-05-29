#include <iostream>
#include <cstdio>
#include <bits/stdc++.h>
using namespace std;


int main (){
	ios_base::sync_with_stdio(false);
	bool bContinue = true;

	while (bContinue){
		int iLetters, iSize;
		string sOriginal;
		string sNew = "";
		string sAdd;

		cin >> iLetters;

		if (iLetters != 0){
			cin >> sOriginal;
			iSize = sOriginal.length() - 1;
			iLetters = (iSize + 1) /iLetters;

			for (int iK = iSize, iL = 0; iK >= 0; iK --){
				sAdd = sAdd + sOriginal[iK];
				iL ++;
				if (iL == iLetters){
					sNew = sAdd + sNew;
					sAdd = "";
					iL = 0;
				}
			}	
			printf("%s\n", sNew.c_str());
		}
		else{
			bContinue = false;
		}
	}
	return 0;
}