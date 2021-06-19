#include <iostream>
#include <vector>
#include <map>
using namespace std;

int NthFibonacci(int n)
{

	if (n == 1 || n == 2)
		return n - 1;
	return NthFibonacci(n - 1) + NthFibonacci(n - 2);
}

map<int, int> dp;

int memFibonacci(int n)
{

	if (n == 1 || n == 2)
		return n - 1;
	if (dp.find(n) == dp.end())
		dp.insert({n, memFibonacci(n - 1) + memFibonacci(n - 2)});
	return dp[n];
}

int top_down(int n)
{

	if (n == 1 || n == 2)
		return n - 1;

	int a = 0;
	int b = 1;
	for (int i = 2; i < n; i++)
	{

		a = b;
		b = a + b;
	}
	return b;
}

int main(){


	printf("%d",memFibonacci(8));

	return 0;
}