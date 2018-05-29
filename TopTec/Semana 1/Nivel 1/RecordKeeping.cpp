#include <iostream>
#include <cstdio>
#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

int equalArraysPos (string iMatr[][3], int iSizeM, string iArra[]){
	for (int iR = 0; iR < iSizeM; iR ++){
		if (iMatr[iR][0] == iArra[0] && iMatr[iR][1] == iArra[1] && iMatr[iR][2] == iArra[2]){
			return iR;
		}
	}
	return -1;
}

int main (){
	int iN;
	int iSizeM = 0;
	scanf("%i", &iN);


	string Matriz[1010][3];
	int iArraV[1010];

	for (int i = 0; i < iN; i++){
		string sArra[3];
		string s1, s2, s3;
		cin >> s1 >> s2 >> s3;
		sArra[0] = s1;
		sArra[1] = s2;
		sArra[2] = s3;
		sort(begin(sArra), end(sArra));

		int iPos = equalArraysPos(Matriz, iSizeM, sArra);
		if (iPos >= 0){
			iArraV[iPos] = iArraV[iPos] + 1;
		}
		else{
			Matriz[iSizeM][0] = sArra[0];
			Matriz[iSizeM][1] = sArra[1];
			Matriz[iSizeM][2] = sArra[2];
			iArraV[iSizeM] = 1;
			iSizeM = iSizeM + 1;
		}
	}
	int Max = 0;
	for (int i = 0; i < iSizeM; i++){
		if(iArraV[i] > Max)
			Max = iArraV[i];
	}
	printf("%i \n", Max);
	return 0;
}