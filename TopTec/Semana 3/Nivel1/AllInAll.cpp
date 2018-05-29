#include <iostream>
using namespace std;

int main (){
	int uno = 0, dos = 0, tres = 0;
	string numeros;
	cin >> numeros;
	int largonumeros = numeros.length();
	bool inicio = false;
	for (int i = 0; i < largonumeros; i +=2){
		if(numeros[i] == '1')
			uno ++;
		else if(numeros[i] == '2')
			dos ++;
		else
			tres ++;
	}

	if(uno != 0)
		inicio = true;

	for(int i = 0; i < uno; i++){
		printf("1");
		if (!(i == uno-1))
			printf("+");
	}

	if(dos != 0){
		if(inicio)
			printf("+");
		inicio = true;}
		

	for(int i = 0; i < dos; i++){
		printf("2");
		if (!(i == dos-1))
			printf("+");
	}

	if(tres != 0){
		if(inicio)
			printf("+");
		inicio = true;}

	for(int i = 0; i < tres; i++){
		printf("3");
		if (!(i == tres-1))
			printf("+");
	}
	return 0;
}