#include<bits/stdc++.h>
using namespace std;
int main()
{
  int n;
  cin>>n;
  string s="";
  while(n>0)
  {
    s+=to_string(n%2);
    n=n/2;
  }
  reverse(s.begin(),s.end());
  cout<<s;
  return 0;
}