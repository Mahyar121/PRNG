#include <iostream>
#include <string>
using namespace std;


int main()
{ 
	int a[15] = { 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 1, 2, 100, 199, 200 };
	int b[15] = { 100, 100, 100, 100, 100, 1, 2, 100, 199, 200, 100, 100, 100, 100, 100 };
	int c[15] = { 1, 2, 100, 199, 200, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100 };

	for (int i = 0; i < 14; i++)
	{

			if ((a[i] == b[i]) && (b[i] == c[i]))
			{
				cout << "Equilateral" << endl;
			}
			else if ((a[i] == b[i]) && (a[i] != c[i]))
			{
				cout << "Isosceles" << endl;
			}
			else if ((a[i] != b[i]) && (a[i] != c[i]) && (b[i] != c[i]))
			{
				cout << "Scalene" << endl;
			}	
			else
			{
				cout << "Not a Triangle" << endl;
			}
	}
	system("Pause");
	return 0;
}