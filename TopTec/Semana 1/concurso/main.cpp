#include <vector>
#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int iN, iG;
    scanf ("%i %i", &iN, &iG);
    vector<int> iRooms(iN, 0);
    //int iRooms1Guest[110];
    bool empty = false;
    for (int i = 0, j = 0, iE = 0; i < iG; i++){
        //cout << "i: " << i;
        int iArraPos1[110];
        int iGuests;
        scanf("%i", &iGuests);
        int iCant, iResidual;
        iCant = iGuests / 2;
        iResidual = iGuests % 2;

        for (int it = 0; it < iCant; it++ ) {
            iRooms[j] = 2;
            iGuests = iGuests -2;
            j++;
            if(j == iN){
                cout << "iGuests" << iGuests << endl;
                empty = true;
                iResidual = 0;
                break;
            }
        }
        if(iResidual == 1){
            cout << "iresudial" << endl;
            iArraPos1[iE] = j;
            cout << "psocion con 1: " << j << endl;
            iRooms[j] = 1;
            j++;
            iE++;
            iGuests = iGuests -1;
            if(j == iN){
                empty = true;
                //break;
            }
        }
        if(empty){
            cout <<"empty" << endl;
            for (int iK = 0; iK < iGuests; iK ++){
                iRooms[iArraPos1[iK]] = 2;
            }
        }

    }

    cout << endl;
    for (int i = 0; i < iN; i++){
        cout <<iRooms[i] << endl;
    }


    return 0;
}