#include <iostream>
using namespace std;

int main()
{

  int n, m;
  int **A;
  // making a double pointer

  cout << "Enter the number of arrays: ";
  cin >> n;

  cout << "Enter the size of each array: ";
  cin >> m;

  A = new int *[n];
  // creating an array of pointers in heap which will have n arrays

  // A[0] = new int[4];
  // A[1] = new int[4];
  // A[2] = new int[4];

  for (int i = 0; i < n; i++)
  {
    A[i] = new int[m];
    // creating arrays of size m and making A[i] point to it
  }

  // now taking all the values
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      cout << "Enter the value of " << i << "," << j << " :";
      cin >> A[i][j];
    }
  }

  // printing all the values
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      cout << A[i][j] << " ";
    }
    cout << endl;
  }

  //// very important: deleting pointer from heap to stop the leak
  for (int i = 0; i < n; i++)
  {
    delete[] A[i];
    // first deleting all the inside pointer pointing to arrays
  }

  // //// very important: deleting pointer from heap to stop the leak
  // for (int i = 0; i < n; i++)
  // {
  //   delete[] A[i];
  //   // first deleting all the inside pointer pointing to arrays
  // }


  // now deleting main pointer in heap
  delete[] A;

  return 0;
}