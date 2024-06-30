/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
using namespace std;

struct Rectangle {

int length;
int breadth;
};

int main()
{
 // cout<<"Hello World";
   
// making a struture: 
//   struct Rectangle r = {10,20};
//   cout<<r.length<<endl;
//   cout<<r.breadth<<endl;

// making a pointer for a structure:    
//   Rectangle *p = &r;
//   cout<<p->length<<endl;
//   cout<<p->breadth<<endl;


// making an aray using pointer in heap:
// int *p = new int[5];
// p[0]= 1;
// p[1]= 11;
// p[2]= 111;
// p[3]= 1111;
// p[4]= 11111;
// for(int i = 0; i<5; i++){
//     cout<<p[i]<<endl;
// }

//making a structure in heap using pointer
// we can do Rectangle *p1= new Rectangle;
//same as

Rectangle *p1;
p1=new Rectangle;

p1->length=14;
p1->breadth=26;

cout<<p1->length<<endl;
cout<<p1->breadth<<endl;
   
   return 0;
   
}