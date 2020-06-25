#ifndef MY_TENSORS_H
#define MY_TENSORS_H
#include<vector>
#include<iostream>

using namespace std;

class V{
	public:
    vector<double> num;
    int size = 0;
  public:
    V();
    V(int n);
    V(const V& b);
    ~V();

    operator bool(){
      bool result = false;
      for(int i=0; i<size;i++){
        result = result||num[i];
      }
      return result;
    }

    bool operator==(V& b){
      if(b.size!=size) return false;
      for(int i=0;i<size;i++){
        if(abs(num[i]-b.num[i])>0.1)
          return false;
      }
      return true;
    }

    double& operator[](int n){
      if(n<0||n>=size){
        cout<<" vector cross the boardary"<<endl;
      }
      else{
        return num[n];
      }
    }

    V& operator=(const V& b){
      size = b.size;
      num = b.num;
      return *this;
    }

    double dot_product(V& b);

    V multiproduct(double n);
};


class matrix{
  public:
    int row=0;
    int col=0;
  public:
    vector<V> arr;
  public:
    matrix();
    ~matrix();
    matrix(const matrix& b);
    matrix(int m, int n);

    V& operator[](int n){
      if(n<0 || n>=row){
        cout<<"matrix corss boundary"<<endl;
      }
      else{
        return arr[n];
      }
    }

    V multiply(V& b);
};
#endif /* MY_TENSORS_H */