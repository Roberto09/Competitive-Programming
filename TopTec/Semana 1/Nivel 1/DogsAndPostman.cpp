#include <iostream>
#include <cstdio>
#include <bits/stdc++.h>
using namespace std;


int main (){
	int A, B, C, D,
		P, M, G;
	scanf("%i %i %i %i %i %i %i", &A, &B, &C, &D, &P, &M, &G);

	int range1 = A + B;
	int range2 = C + D;

	int ModuleP1 = P % range1;
	int ModuleM1 = M % range1;
	int ModuleG1 = G % range1;

	int ModuleP2 = P % range2;
	int ModuleM2 = M % range2;
	int ModuleG2 = G % range2;

	bool D1 = true;
	bool D2 = true;


	// P
	if (ModuleP1 == 0 || ModuleP1 >= A+1){
		D1 = false;
	}
	if(ModuleP2 == 0 || ModuleP2 >= C+1){
		D2 = false;
	}
	if(D1 && D2)
		printf("both\n");
	else if (D1 || D2)
		printf("one\n");
	else
		printf("none\n");


	D1 = true;
	D2 = true;

	// M
	if (ModuleM1 == 0 || ModuleM1 >= A+1){
		D1 = false;
	}
	if(ModuleM2 == 0 || ModuleM2 >= C+1){
		D2 = false;
	}
	if(D1 && D2)
		printf("both\n");
	else if (D1 || D2)
		printf("one\n");
	else
		printf("none\n");


	D1 = true;
	D2 = true;

	// G
	if (ModuleG1 == 0 || ModuleG1 >= A+1){
		D1 = false;
	}
	if(ModuleG2 == 0 || ModuleG2 >= C+1){
		D2 = false;
	}
	if(D1 && D2)
		printf("both\n");
	else if (D1 || D2)
		printf("one\n");
	else
		printf("none\n");
}