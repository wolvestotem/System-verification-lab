#include "Matrix.h"
  
int main(int argc, char* argv[]) {
	string matrix1 = argv[1];
	string matrix2 = argv[2];
	ifstream mx1(matrix1);
	ifstream mx2(matrix2);
    ifstream mx3(argv[3]);

	int row1,col1,row2,col2,row3,col3;
	mx1>>row1>>col1;
	mx2>>row2>>col2;
    mx3>>row3>>col3;
	Matrix m1(row1,col1);
	Matrix m2(row2,col2);
    Matrix m3(row3,col3);

	for(int i=0;i<row1;i++){
		for(int j=0;j<col1;j++)
			mx1>>m1.num[i][j];
	}
	for(int i=0;i<row2;i++){
		for(int j=0;j<col2;j++)
			mx2>>m2.num[i][j];
	}
  for(int i=0;i<row3;i++){
		for(int j=0;j<col3;j++)
			mx3>>m3.num[i][j];
	}

	Matrix res(row1,col2);
	for(int i=0;i<row1;i++){
		for(int j=0;j<col2;j++){
			for(int k=0;k<col1;k++){
				res.num[i][j] += m1.num[i][k]*m2.num[k][j];
			}
		}
	}

  for(int i=0;i<row3;i++){
    for(int j=0;j<col3;j++){
      res.num[i][j] += m3.num[i][j];
    }
  }
	// cout << res.num.size() << " " << res.num[0].size()<<endl;
	ofstream r;
	r.open("result.txt");
	r<<row1<<" "<<col2;
	r<<endl;
	for(int i=0;i<row1;i++){
		for(int j=0;j<col2;j++){
			r<<res.num[i][j]<<" ";
		}
		r<<endl;
	}
	r.close();
	mx1.close();
	mx2.close();
    mx3.close();
	return 0;
} 
