// #include <iostream>
// using namespace std;

// // we are calculating e^x for different x and running to different n times for accuracy
// double e(double x, double n)
// {

//   static double s = 1;

//   if (n == 0)
//   {
//     return s;
//   }

//   s = 1 + ((x / n) * s);

//   return e(x, n - 1);
// }
// int main()
// {

//   double x = 2;
//   double n = 100000;

//   cout << e(x, n) << endl;
// }

//*************

#include <iostream>
using namespace std;

double e(double x, double n)
{
  double s = 1;

  for (n; n > 0; n--)
  {
    s = 1 + x / n * s;
  }

  return s;
}
int main()
{

  cout << e(2, 1000) << endl;
  return 0;
}