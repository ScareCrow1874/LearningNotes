#include <iostream>

using namespace std;

int main()
{
 label0:
  cout << "IDONB" << endl;
  int a = 3;
  int b = 53;

  if (a < b) {
    goto label2;
  }

 label1:
  cout << "ABC" << endl;
 label2:
  cout << "SDB" << endl;
}

