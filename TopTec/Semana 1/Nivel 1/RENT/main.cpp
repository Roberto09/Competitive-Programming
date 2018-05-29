#include <iostream>

using namespace std;

struct plane{
    int start;
    int end;
    int price;
};

int main() {
    plane planes[10010];
    int iArraBP[10010];
    int iNPlanes;
    scanf("%i", &iNPlanes);

    for (int p = 0; p < iNPlanes; p++){
        int start, duration, price;
        scanf("%i %i %i", &start, &duration, &price);
        planes[p].start = start;
        planes[p].end = start + duration;
        planes[p].price = price;
    }

    for (int p = 0; p < iNPlanes; p++){
        for (int p2 = p+1; p2 < iNPlanes; p2++){

        }
    }

    return 0;
}