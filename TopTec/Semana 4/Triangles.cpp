#include <iostream> 
#include <vector>
#include <math.h> 
using namespace std;

struct posicion
{
	int iX;
	int iY;
};


double calcularPendiente(posicion pos1, posicion pos2){
	int iX1, iX2, iY1, iY2;
	iX1 = pos1.iX;
	iY1 = pos1.iY;
	iX2 = pos2.iX;
	iY2 = pos2.iY;

	double pendiente = (iY2 - iY1) / ((iX2 - iX1)*1.0);
	return pendiente; 
}

int SumatoriaTortal(int iN){
	int sumaTotal = 0;
	int iV = iN +1;
	vector<posicion> posiciones((iV*iV));

	int index = 0;
	for(int iR = 0; iR < iV; iR ++){
		for(int iC = 0; iC < iV; iC ++){
			//cout << iR << ", " << iC << endl;
			posiciones[index].iX = iR;
			posiciones[index].iY = iC;
			index ++;
		}
	}
	//Primer punto
	for(int i1 = 0; i1 < (iV*iV); i1++){
		//Segundo punto
		for(int i2 = i1+1; i2< (iV*iV); i2 ++){
			double p1p2Slope = calcularPendiente(posiciones[i1], posiciones[i2]);
			//TercerPunto
			for(int i3 = i2+1; i3 < (iV*iV); i3 ++){
				double p2p3Slope = calcularPendiente(posiciones[i2], posiciones[i3]);
					if (p1p2Slope == p2p3Slope)
						sumaTotal ++;
			}
		}
	}

return sumaTotal;
}
int main (){
	int iCasos;
	scanf("%i", &iCasos);
	for(int i = 1; i <= 10; i++){
		int x = i;
		x = (x+1) * (x+1);
		x = ((x) * (x-1) * (x-2)) / 6;
		cout << x - SumatoriaTortal(i) << ", ";
	}	
	return 0;
}