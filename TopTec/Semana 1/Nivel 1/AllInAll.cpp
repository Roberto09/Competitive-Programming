#include <iostream>
ios_base::sync_with_stdio(false);
cin.tie(NULL);

using namespace std;

bool validString (string s, string t, int lenS, int lenT){
	if (lenS > lenT)
		return false;
	int iS = 0;
	for (int iT = 0; iT < lenT && iS < lenS; iT++){
		if (s[iS] == t[iT]){
			iS ++;
		}
	}
	if (iS == lenS)
		return true;
	else
		return false;
}

int main (){
	string s, t;
	int lenS, lenT;
	while (cin >> s){
	cin >> t;
	lenS = s.length();
	lenT = t.length();


	if (validString(s,t,lenS,lenT))
		printf("%s", "Yes\n");
	else
		printf("%s", "No\n");

	}
	return 0;
}