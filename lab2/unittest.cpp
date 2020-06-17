#define CATCH_CONFIG_MAIN
#include "catch.hpp"

#include "Matrix.h"


/* Test cases provided only for reference.
 * Feel free to use your own grouping of tests scenarios
 */
TEST_CASE("Test Vector Class"){
	Vector v;
  Vector u;
	SECTION("constructor"){
		REQUIRE(v.gethead() == nullptr);
	}
  SECTION("set get"){
    v.set(0,10);
    v.set(0,20);
    v.set(4,4);
    v.set(3,8);
    v.set(10,10);
    v.set(4,10);
    v.set(5,5);
    CHECK(v.get(0)==20);
    CHECK(v.get(4)==10);
    CHECK(v.get(3)==8);
    CHECK(v.get(10)==10);
    CHECK(v.get(5)==5);
  }
  SECTION("dot production"){
    u.set(0,2);
    u.set(1,2);
    u.set(5,8);
    u.set(3,2);
    v.set(0,10);
    v.set(0,20);
    v.set(4,4);
    v.set(3,8);
    v.set(10,10);
    v.set(4,10);
    v.set(5,5);
    CHECK(v.dot(u)==96);
  }
}


TEST_CASE("Test Matrix Class"){
  Matrix m1(2,3,ROW_MAJOR);
  Matrix m2(3,2,COL_MAJOR);
  SECTION("constructor"){
    CHECK(m1.m==2);
    CHECK(m1.n==3);
    CHECK(m1.getformat()==ROW_MAJOR);
    CHECK(m1.getarray());
  }
  SECTION("set get"){
    m1.set(0,0,1);
    m1.set(0,1,2);
    m1.set(1,2,3);
    m2.set(0,0,2);
    m2.set(0,1,4);
    m2.set(1,0,5);
    m2.set(2,0,3);
    CHECK(m1.get(1,2)==3);
    CHECK(m1.get(0,2)==0);
    CHECK(m2.get(0,0)==2);
    CHECK(m2.get(10,10)==0);
    CHECK(m1.get(10,10)==0);
  }
  SECTION("matrix multiplication"){
    m1.set(0,0,1);
    m1.set(0,1,2);
    m1.set(1,2,3);
    m2.set(0,0,2);
    m2.set(0,1,4);
    m2.set(1,0,5);
    m2.set(2,0,3);
    CHECK(m1.multiply(m2).get(0,0)==12);
    CHECK(m1.multiply(m2).get(0,1)==4);
    CHECK(m1.multiply(m2).get(1,0)==9);
    CHECK(m1.multiply(m2).get(1,1)==0);
  }
}
