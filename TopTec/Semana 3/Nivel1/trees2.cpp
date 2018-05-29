#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

struct apuntador{
	int EsAPuntadoPor = -1;
};
int main (){
	int index = 1;
	while (true){

		bool MasDeUnAP = false;
		bool Valido = false;
		bool Acabo = false;
		unordered_map<int, apuntador> map;

		while(true){
			int P1, P2;
			scanf("%i %i", &P1, &P2);
			if(P1 == 0)
				break;
			if(P1 < 0 || P2 < 0){
				Acabo = true;
				break;
			}

			if (map[P2].EsAPuntadoPor > 0 || P1 == P2){
				MasDeUnAP = true;
			}
			map[P2].EsAPuntadoPor = P1;
			map[P1];
		}

		if (Acabo)
			break;

		if(MasDeUnAP){
			printf("Case %i is not a tree.\n", index);
			index ++;
			continue;
		}


	int roots = 0;
		for (unordered_map<int, apuntador>::const_iterator it = map.begin(); it != map.end(); ++it)
			{
				//cout << it -> first <<  " es apuntado por: " << it -> second.EsAPuntadoPor << endl;
				if(it -> second.EsAPuntadoPor == -1){
					//cout << "valido = true" << endl;
					roots ++;
				}
			}

		if(roots == 1)
			Valido = true;

		if(Valido || map.size() == 0)
			printf("Case %i is a tree.\n", index);
		else
			printf("Case %i is not a tree.\n", index);
		index ++;

	}

	return 0;
}