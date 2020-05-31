#include<vector>
#include<iostream>
#include<fstream>
#include<string>

#ifndef MY_MATRIX_H
#define MY_MATRIX_H


using namespace std;

class Matrix {

  /* List class attributes */
	int row_;
	int col_;
	

	public:
	vector<vector<int>> num;
	Matrix(int row, int col): row_(row),col_(col),num(row,vector<int>(col)) {}
    
    /* List class methods */
    
};

#endif /* MY_MATRIX_H */
// Changed
// Changed
