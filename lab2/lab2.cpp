#include "Matrix.h"
  
int main(int argc, char* argv[]) 
{ 
  string file1 = argv[1];
  string flie2 = argv[2];

  ifstream f1(file1);
  ifstream f2(flie2);

  int m1,n1, m2,n2;
  f1>>m1>>n1;
  f2>>m2>>n2;
  Matrix arr1(m1,n1,ROW_MAJOR);
  Matrix arr2(m2,n2,COL_MAJOR);

  int tem;
  for(int i=0; i<m1; i++){
    for(int j=0; j<n1; j++){
      f1>>tem;
      if(tem){
        arr1.set(i,j,tem);
      }
    }
  }
  for(int i=0; i<m2; i++){
    for(int j=0; j<n2; j++){
      f2>>tem;
      if(tem){
        arr2.set(i,j,tem);
      }
    }
  }
  Matrix result = arr1.multiply(arr2);
  cout<<result.m<<' '<<result.n<<endl;;
  
  ofstream f3;
  f3.open("result.txt");
  f3<<m1<<' '<<n2<<endl;
  for(int i=0; i<result.m; i++){
    for(int j=0; j<result.n; j++){
      f3<<result.get(i,j)<<' ';
    }
    f3<<endl;
  }
  f1.close();
  f2.close();
  f3.close();
  return 0;
} 