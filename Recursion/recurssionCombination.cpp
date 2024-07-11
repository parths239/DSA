#include <iostream>
using namespace std;

// made my own nCr that follows Pascal triangle method
int nCr(int n, int r)
{
  int total;

  // in pascal triangle for first and last element nCr is 1
  if (r == 0 || n == r)
  {
    total = 1;
  }

  // for rest its the total of above two
  else
  {
    total = nCr(n - 1, r - 1) + nCr(n - 1, r);
  }

  return total;
}
int main()
{

  cout << "nCr is here:" << endl;
  cout << nCr(4, 2) << endl;
  return 0;
}