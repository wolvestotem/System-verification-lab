#include "Matrix.h"

/**
 * Constructor. Assigns NULL to head.
 */
Vector::Vector(){
	head = nullptr;
}

/**
 * Destructor. Deletes the elements of the linked list.
 */
Vector::~Vector(){
  // delete head->next;
  // delete head;
  // cout<<"delete head"<<endl;
}

/**
  * Inserts or updates an element of the list.
  * Insertion mentains the list sorted by index.
  */
void Vector::set(int index, int value){
  if(!head || head->index>index){
    Element *tem = new Element(index,value);
    tem->next = head;
    head = tem;
  }
  else{
    Element *curr(head);
    Element *pre = new Element(-1,0);
    pre->next = head;
    while(curr->index<index && curr && curr->next){
      curr = curr->next;
      pre = pre->next;
    }

    if(curr->index == index){
      curr->value = value;
    }
    else if(curr->index<index){
      curr->next = new Element(index,value);
    }
    else{
      Element *tem = new Element(index,value);
      pre->next = tem;
      tem->next = curr;
    }
  }
}

/**
 * Retrieves the element of the list with the specified index.
 * Returns 0 if index not found since only non zero elements are stored.
 */
int Vector::get(int index){
  if(!head) return 0;
  Element *curr(head);
  while(curr && curr->index<index){
    curr = curr->next;
  }
  if(!curr || curr->index>index)
    return 0;
  else{
    return curr->value; 
  }
}

/**
 * Return the results of the vector dot product.
 */
int Vector::dot(Vector v){
  if(!head) return 0;
  Element *curr(head);
  int result = 0;
  while(curr){
    int val = v.get(curr->index);
    result += curr->value*val;
    curr = curr->next;
  }
  return result;
}

  
/**
 * Constructor. Allocates a Vector array of size
 * m or n depending of the storage format.
 * https://en.wikipedia.org/wiki/Row-_and_column-major_order
 */
Matrix::Matrix(int row, int col, int form):m(row),n(col),format(form) {
  if(format==ROW_MAJOR){
    data = new Vector[m];
  }
  else{
    data = new Vector[n];
  }
};

/**
 * Destructor. Deletes the Vector array.
 */
Matrix::~Matrix(){

}

/**
 * Inserts or updates an element of the Matrix.
 */
void Matrix::set(int row, int column, int value){
  if(format==ROW_MAJOR){
    data[row].set(column,value);
  }
  else{
    data[column].set(row,value);
  }
}

/**
 * Retrieves the element of the Matrix.
 */
int Matrix::get(int row, int column){
  if(format==ROW_MAJOR){
    if(row>=m)
      return 0;
    else{
      return data[row].get(column);
    }
  }
  else{
    if(column>=n)
      return 0;
    else{
      return data[column].get(row);
    }
  }
}

/**
 * Return the results of the Matrix multiplication.
 */
Matrix Matrix::multiply(Matrix arr){
  Matrix result(m,arr.n,ROW_MAJOR);
  for(int i=0; i<m ;i++){
    // int val = 0;
    for(int j=0; j<arr.n; j++){
      result.set(i,j,data[i].dot(arr.data[j]));
    }
  }
  return result;
}
