#include "Tensors.h"

#include"Tensors.h"

V::V(){}

V::V(int n){
  size = n;
  num = vector<double>(n,0);
}

V::V(const V& b){
  size = b.size;
  num = b.num;
}

V::~V(){

}


double V::dot_product(V& b){
  double result=0;
  if(b.size!=size){
    cout<<"error in dot product: size cannot match"<<endl;
  }
  else{
    for(int i=0;i<size;i++){
      result+=num[i]*b.num[i];
    }
  }
  return result;
}

V V::multiproduct(double n){
  V res(size);
  for(int i=0; i<size;i++){
    res[i] = num[i]*n;
  }
  return res;
}

matrix::matrix(){}

matrix::matrix(int m,int n){
  row=m;
  col=n;
  arr=vector<V>(row,V(col));
}

matrix::matrix(const matrix& b){
  row = b.row;
  col = b.col;
  arr = b.arr;
}

matrix::~matrix(){

}

V matrix::multiply(V& b){
  V result(row);
  if(col!=b.size){
    cout<<"multiply error: not match"<<endl;
  }
  else{
    for(int i=0;i<row;i++){
      result[i] = arr[i].dot_product(b);
    }
  }
  return result;
}