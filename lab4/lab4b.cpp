#include <fstream>

using namespace std;

int main(int argc, char* argv[]) 
{ 

  ofstream fileout("./result.txt");

  fileout.close();

  return 0;
}