#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

struct point{
    int id;
    int x;
    int y;
};

double distance(point p1, point p2){

    int x = abs(p1.x-p2.x);
    int y = abs(p1.y-p2.y);
    return (sqrt(pow(x,2)+ pow(y,2)));
}

double MinDist = std::numeric_limits<double>::max();


void totalDistance(int vecLen, vector<point> pts, double SumaAcumulada, point ptoAnterior, point ptoFinal){
    for (int iK = 0; iK < vecLen; iK ++){
        double NuevaSumaAcumulada = SumaAcumulada + distance(ptoAnterior, pts[iK]);
        if (NuevaSumaAcumulada > MinDist)
            break;
        int NuevoVecLen = vecLen - 1;

        vector<point> mdPoints = pts;
        std::swap(mdPoints[iK], mdPoints.back());
        mdPoints.pop_back();

        if(vecLen == 1){
            NuevaSumaAcumulada = NuevaSumaAcumulada + distance(pts[iK], ptoFinal);
            if(NuevaSumaAcumulada < MinDist){
                MinDist = NuevaSumaAcumulada;
            }
        }
        totalDistance(NuevoVecLen, mdPoints, NuevaSumaAcumulada, pts[iK], ptoFinal);
    }
}


//bool sortById(const point &p, const point &q) { return p.id < q.id; }

int main() {
    string hola;
    vector<point> points;
    int iCoordenadas, idStartPoint, idEndPoint;
    point pInicial, pFinal;

    scanf("%i", &iCoordenadas);
    for (int i = 0; i < iCoordenadas; i++) {
        point p;
        scanf("%i %i %i", &p.id, &p.x, &p.y);
        points.push_back(p);
    }
    scanf("%i %i", &idStartPoint, &idEndPoint);


    //sort(begin(points), end(points), sortById);
    for (int i = 0; i < iCoordenadas; i++){
        if (points[i].id == idStartPoint){
            //cout << "eliminar primer id" << endl;
            pInicial.x = points[i].x;
            pInicial.y = points[i].y;
            std::swap(points[i], points.back());
            points.pop_back();
            i --;
            iCoordenadas --;
        }
        else if (points[i].id == idEndPoint){
            //cout << "eliminar ultimo id" << endl;
            pFinal.x = points[i].x;
            pFinal.y = points[i].y;
            std::swap(points[i], points.back());
            points.pop_back();
            i --;
            iCoordenadas --;
        }
    }

    // Comienza Algoritmo
    //cout << iCoordenadas << endl;

    if (iCoordenadas != 0) {
        totalDistance(iCoordenadas, points, 0, pInicial, pFinal);
    }
    else{
        MinDist = distance(pInicial, pFinal);
    }

    //cout << "La distancia minima fue: " << MinDist << endl;
    printf("%.2f", MinDist);

    return 0;
}