#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

double dT;

int scanMinVal(int currentNode, vector<vector<int>> &nodes){
	//Si es un trabajador...
	//cout << "entre" << endl;
	//cout << currentNode << endl;
	if(nodes[currentNode].size() == 0){
		//cout << "return 1" << endl;
		return 1;
	}
	//Si es un boss
	int minSum = 0;
	int minN =  (int) ceil (nodes[currentNode].size() * dT);

	vector<int> posibleN;
	for(int i = 0; i < nodes[currentNode].size(); i ++){
		int node = nodes[currentNode][i];
		posibleN.push_back(scanMinVal(node, nodes));
	}

	//cout << "--- sort begin" << endl;
	sort(posibleN.begin(), posibleN.end());
	for(int iK = 0; iK < minN; iK ++){
		minSum += posibleN[iK];
	}
	return minSum;
}


int main (){
	while (true){
		int iN;
		scanf("%i %lf", &iN, &dT);
		if(iN == 0)
			break;
		dT = dT / 100.0;
		vector<vector<int>> nodes(iN+1);
		for(int i= 1; i <= iN; i++){
			int iNum;
			scanf("%i", &iNum);
			nodes[iNum].push_back(i);
		}

		for(int i = 0; i < nodes[0].size(); i++){
			int node = nodes[0][i];
			//cout << node << endl;
		}
		//cout << "flag" << endl;
		printf("%i \n", scanMinVal(0, nodes));
	}
	return 0;
}