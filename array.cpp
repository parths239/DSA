#include<iostream>
using namespace std;

int main()
{

 int A[5] = {1,2,3};
 
  int i;
  for(i=0;i<5;i++)
  {
    cout<<A[i]<<endl;
  }

  for(int x:A)
  {
    cout<<x<<endl;
  }
  cout<<A[4];
  return 0;
}
