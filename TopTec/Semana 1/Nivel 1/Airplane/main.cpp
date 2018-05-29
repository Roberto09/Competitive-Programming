#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct plane {
    int MAXPrice;
    int inicio;
    int final;
    int ganancia;
};

int iMaxValueFinder (int vecLen, vector<plane> &plns, int plnAct){
    int SuperMaxValue = 0;
    for (int iK = plnAct; iK < vecLen; iK++){
        if(plns[iK].MAXPrice < 0) {
            int MaxValue = plns[iK].ganancia;
            for (int i = iK + 1; i < vecLen; i++) {
                if (plns[iK].final <= plns[i].inicio) {
                    int calcValue = plns[iK].ganancia + iMaxValueFinder(vecLen, plns, i);
                    if (calcValue > MaxValue)
                        MaxValue = calcValue;
                }
            }
            plns[iK].MAXPrice = MaxValue;
            if (MaxValue > SuperMaxValue)
                SuperMaxValue = MaxValue;
        }
        else{
            if(plns[iK].MAXPrice > SuperMaxValue)
                SuperMaxValue = plns[iK].MAXPrice;
        }

    }
    return SuperMaxValue;
}

bool sortById(const plane &p, const plane &q) { return p.inicio < q.inicio; }

int main() {

    int CasosTotales;
    scanf("%i", &CasosTotales);
    for (int i = 0; i < CasosTotales; i++) {
        vector<plane> planes;
        int largo;
        scanf("%i", &largo);
        for (int i = 0; i < largo; i++) {
            plane p;
            p.MAXPrice = -1;
            int iDuracion;
            scanf("%i %i %i", &p.inicio, &iDuracion, &p.ganancia);
            p.final = p.inicio + iDuracion;
            planes.push_back(p);
        }
        sort(planes.begin(), planes.end(), sortById);
        printf("%i", iMaxValueFinder(largo,planes,0));
    }
    return 0;
}