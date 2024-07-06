#include <iostream>
using namespace std;

int e(int x, int n)
{
  static int p = 1;
  static int f = 1;
  int r;

  if (n == 0)
  {
    return 1;
  }
  else
  {
    r = e(x, n - 1);
    p = p * x;
    f = f * n;

    return (r + (p / f));
  }
};
int main()
{
  int x, n;
  cout << "This is the Taylor series example:" << endl;
  cout << "We will calculate e^x, so please enter the value for x:" << endl;
  cin >> x;
  cout << "To calculate e^x, we also need a number n which helps determine accurate value for the series " << endl;
  cout << "so please also enter the value of n:" << endl;
  cin >> n;

  cout << "The values if e^" << x << " for the value of " << n << " is " << e(x, n);
}

////////////*********************//////

// This was my method

//     #include <stdio.h>
//     #include <stdlib.h>

//     int factorial(int n)
//     {
//     if(n>1)
//     return n*factorial(n-1);
//     return 1;
//     }

//     int power(int num, int n)
//     {
//     if(n==0)
//     return 1;
//     if(n>0)
//     return num*power(num, n-1);
//     return 0;
//     }

//     double taylorSeries(int x, int n)
//     {
//     if(n==0)
//     return 1;
//     if(n>0)
//     return(float)power(x,n)/factorial(n) + taylorSeries(x,n-1);
//     return 0;
//     }

//     int main()
//     {
//     printf("%d",power(4,2));
//     printf("Taylor Series : %lf",taylorSeries(1,14));
//     return 0;
//     }