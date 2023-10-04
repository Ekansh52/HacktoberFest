#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<stdio.h>
class item{
 int code ;
 char name[25] ;
 int price ;
};
void main()
{
 ofstream fout ;
 fout.open("item.dat", ios::binary) ;
 for()