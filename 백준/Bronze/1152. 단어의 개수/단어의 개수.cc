#include <iostream>
#include <string>
using namespace std;

int main() {
	string s1;
	getline(cin, s1);
	int n = 0;
	for (int i = 0; i < s1.length(); i++)
		if (s1[i] == ' ')
			n++;
	if (s1[0] == ' ')
		n--;
	if (s1[s1.length() - 1] == ' ')
		n--;
		cout << n + 1;
	
}