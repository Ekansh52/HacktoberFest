#include<iostream.h>
#include<conio.h>
void main()
{
 for(int i=1; i<=4; i++)
 {
  for(int j=1; j<=4-i; j++)
  {
   cout<<" ";
  }
   for(int k=1; k<=i; k++)
    cout<<"*" ;
  cout<<endl ;
 }
 getch () ;
}