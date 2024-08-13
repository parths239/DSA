#include <iostream>
using namespace std;

class Array
{
private:
  int Arr[10];
  int size;

public:
  Array(int *A, int size);
  void print();
};

Array::Array(int *A, int s) : size(s)
{
  // Copy elements from A to Arr while ensuring we do not exceed the bounds of Arr
  for (int i = 0; i < size && i < 10; ++i)
  {
    Arr[i] = A[i];
  }
  // Fill the rest of Arr with a default value (e.g., 0)
  for (int i = size; i < 10; ++i)
  {
    Arr[i] = 0;
  }
}

void Array::print()
{
  for (int i = 0; i < 10; ++i) // Print all elements in the array, since Arr has 10 elements
  {
    cout << " " << Arr[i];
  }
  cout << endl;
}

int main()
{
  int *p = new int[10]; // Allocate memory for 10 integers

  // Initialize the allocated array
  int initValues[5] = {2, 4, 6, 8, 10};
  for (int i = 0; i < 5; ++i)
  {
    p[i] = initValues[i];
  }

  Array A(p, 5);

  A.print();

  delete[] p; // Deallocate the memory
  return 0;
}
