#ifndef MY_MATRIX_H
#define MY_MATRIX_H

#define ROW_MAJOR 0
#define COL_MAJOR 1

#include<iostream>
#include<fstream>
#include<string>

using namespace std;

/**
 * Structure to represent the elements of a Vector.
 * Since the Vector class does not store zero elements
 * we use index to know the position of the element.
 */
struct Element{
  int index;
  int value;

  Element* next;
  Element(int ind, int val):index(ind),value(val),next(nullptr) {}
};


/**
 * Vector class that stores only non zero elements.
 */
class Vector{

private:
  /**
   * Head element of the linked list. Elements are sorted by index.
   */
  Element *head;

public:
  /**
   * Constructor. Assigns NULL to head.
   */
  Vector();

  /**
   * Destructor. Deletes the elements of the linked list.
   */
  ~Vector();

  /**
   * Inserts or updates an element of the list.
   * Insertion mentains the list sorted by index.
   */
  inline Element* gethead(){
    return head;
  }

  void set(int index, int value);

  /**
   * Retrieves the element of the list with the specified index.
   * Returns 0 if index not found since only non zero elements are stored.
   */
  int get(int index);

  /**
   * Return the results of the vector dot product.
   */
  int dot(Vector v);
};


class Matrix {

private:
  int format;  // ROW_MAJOR or COL_MAJOR
  Vector *data;

public:
  /**
   * Matrix dimensions. Useful for printing.
   */
  int m, n;
  
  /**
   * Constructor. Allocates a Vector array of size
   * m or n depending of the storage format.
   * https://en.wikipedia.org/wiki/Row-_and_column-major_order
   */
  Matrix(int row, int col, int form);

  /**
   * Destructor. Deletes the Vector array.
   */
  ~Matrix();

  inline int getformat(){
    return format;
  }

  inline Vector* getarray(){
    return data;
  }

  /**
   * Inserts or updates an element of the Matrix.
   */
  void set(int row, int column, int value);

  /**
   * Retrieves the element of the Matrix.
   */
  int get(int row, int column);

  /**
   * Return the results of the Matrix multiplication.
   */
  Matrix multiply(Matrix arr);
};

#endif /* MY_MATRIX_H */
