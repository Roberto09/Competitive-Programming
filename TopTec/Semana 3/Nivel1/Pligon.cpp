#include <iostream> 
using namespace std;

int main (){
	unsigned long long iD, iL;
	scanf("%llu %llu", &iD, &iL);
	iL -=2;
	if (((iL*(iL+1))/2)-1 == iD)
		printf("yes");
	else
		printf("no");
}