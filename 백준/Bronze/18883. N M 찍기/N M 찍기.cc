#include <iostream>
using namespace std;
int main(){
  int n, m, cnt=1;
  cin>>n>>m;
  for(int i=0; i<n; i++)
  {
    for(int j=0; j<m; j++)
    {
      cout<<cnt++;	
      if(j!=m-1)	
        cout<<" ";
    }
    cout<<"\n";
  }
}