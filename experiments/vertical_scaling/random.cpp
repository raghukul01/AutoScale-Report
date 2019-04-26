#include<bits/stdc++.h>
using namespace std;

string str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

string getRandString(int n) {
	string a;
	for(int i = 0;i < n;i++)
		a.push_back(str[rand()%str.length()]);
	return a;
}

int main(int argc, char** argv) {
	ios_base::sync_with_stdio(false),cin.tie(0),cout.precision(17);
	int n;
	int m;
	int valLength;

	n = std::stoi(argv[1]);
    m = std::stoi(argv[2]);
	vector<string> keys, values;

	for(int i = 0; i < n; i++) {
        // value can be of length 1 to 2*m
        valLength = (rand()%(2*m)) + 1;

		keys.push_back(getRandString(m));
		values.push_back(getRandString(valLength));
	}
    freopen("keyVal.txt", "w", stdout);
	for(int i = 0;i < n;i++)
		cout << keys[i] << "," << values[i] << endl;
}
