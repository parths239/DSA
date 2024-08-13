// checks if array is sorted

#include <iostream>

class Array
{
public:
  int A[10]; // Fixed-size array
  int size;
  int length;

  Array(int arr[], int sz, int len) : size(sz), length(len)
  {
    for (int i = 0; i < length; i++)
    {
      A[i] = arr[i];
    }
  }

  void Display() const
  {
    std::cout << "\nElements are\n";
    for (int i = 0; i < length; i++)
    {
      std::cout << A[i] << " ";
    }
    std::cout << std::endl;
  }

  bool isSorted() const
  {
    for (int i = 0; i < length - 1; i++)
    {
      if (A[i] > A[i + 1])
      {
        return false;
      }
    }
    return true;
  }
};

int main()
{
  int arr[] = {2, 3, 9, 16, 18, 21, 28, 32, 35}; // Initialize array
  Array arr1(arr, 10, 9);                        // Create Array object
  std::cout << arr1.isSorted() << std::endl;     // Check if sorted and print result
  arr1.Display();                                // Display elements
  return 0;
}
