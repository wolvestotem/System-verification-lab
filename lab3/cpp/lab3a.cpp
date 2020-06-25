#include "Tensors.h"

#include <fstream>

using namespace std;

int main(int argc, char* argv[]) 
{ 
  ifstream filein1(argv[1]);
  ifstream filein2(argv[2]);
  ofstream fileout("./result.txt");
  int m1,n1,m2,n2;
  filein1>>m1>>n1;
  filein2>>m2>>n2;
  //
  // cout<<m1<<n1<<m2<<n2<<endl;
  matrix m(m1,n1);
  for(int i=0;i<m1;i++){
    for(int j=0;j<n1;j++){
      filein1>>m[i][j];
    }
  }

  // for(int i=0;i<m1;i++){
  //   for(int j=0;j<n1;j++){
  //     cout<<m[i][j]<<' ';
  //   }
  //   cout<<endl;
  // }
  V vin(m2);
  for(int i=0;i<m2;i++){
    filein2>>vin[i];
  }
  // cout<<"VVV"<<endl;
  // for(int i=0;i<m2;i++){
  //   cout<<vin[i]<<' ';
  // }

  // cout<<m.row<<m.col<<vin.size<<endl;

  if(n1!=m2 || m1!=n1){
    fileout<<"Error";
    return 0;
  }
  if(!vin){
    fileout<<"No";
    return 0;
  }
  V res=m.multiply(vin);

  double times;
  int i;
  for(i=0;i<vin.size;i++){
    if(vin[i])
      break;
  }
  times = res[i]/vin[i];
  V tem = vin.multiproduct(times);

  if(res==tem){
    fileout<<times;
  }
  else{
    fileout<<"No";
  }

  filein1.close();
  filein2.close();
  fileout.close();

  return 0;
} 