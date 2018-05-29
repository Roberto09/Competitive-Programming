#include <iostream>
#include <unordered_map>
using namespace std;

struct apuntador{
	int EsAPuntadoPor = -1;
	int apunta = -1;
};
int main (){
	int index = 1;
	bool continua = true;
	while(continua) {
		bool EsValido = true;
		int P1, P2;
		unordered_map<int, apuntador> map;
		//Checa para repetidos
		while(true){
			scanf("%i %i", &P1, &P2);
			if(P1 == 0)
				break;
			if(P1 == -1){
				continua = false;
				break;
			}
			//El P2 apunta al P1
			if(map[P2].EsAPuntadoPor > 0 || P1 == P2){
				EsValido = false;
			}
			map[P2].EsAPuntadoPor = P1;
			map[P1].apunta = P2;
		}

		if (!continua){
			break;
		}

		if(!EsValido){
			printf("Case %i is not a tree.\n", index);
			index ++;
			continue;
		}

		//Checa para roots

		int roots = 0;

		for (unordered_map<int, apuntador>::const_iterator it = map.begin(); it != map.end(); ++it)
		{
			
			if(it -> second.EsAPuntadoPor == -1)
				roots ++;
		}

		if(roots == 0)
			EsValido = false;


		if(!EsValido)
			printf("Case %i is not a tree.\n", index);
		else
			printf("Case %i is a tree.\n", index);

		index ++;
	}
	return 0;
}