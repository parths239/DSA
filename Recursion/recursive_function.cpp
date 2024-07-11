#include <iostream>
using namespace std;

// this is quite interesting
void func(int n)
{
  if (n > 0)
  {
    func(n - 1);
    cout << n << endl;
    func(n - 1);
  }
}
int main()
{
  cout << "hahaha" << endl;

  func(3);
  return 0;
}