#include<iostream>

using namespace std;

int main()
{
int n, m, i, j;
cout << "Enter number of rows: ";
cin >> n;
for(i = 0; i <= n; i++)
{
for(m = n; m > i; m--)
cout << " ";
for(j=0; j<i; j++)
cout << "* ";
cout << "\n";
}
for(i = 1; i < n; i++)
{
for(m = 0; m < i; m++)
cout << " ";
for(j = n; j > i; j--)
cout << "* ";
cout << "\n";// ending line after each row
}
return 0;
}
