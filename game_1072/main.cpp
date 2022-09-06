#include <iostream>

using namespace std;

int main() {
  long long x, y, a_x, a_y;
  long long z, adj_z, a;

  cin >> x >> y;
  if (x == y) {
    cout << "-1" << endl;
    return 0;
  }
  z = (y * 100) / x;

  a = x;
  while (true) {
    a_x = x + a;
    a_y = y + a;
    adj_z = (a_y * 100) / a_x;
    if (adj_z > z + 1) {
      a = a / 2;
    }
    else if(adj_z == z){
      a = a * 2;
    }
    else {
      break;
    }
  }

  while (adj_z != z) {
    a -= 1;
    a_x = x + a;
    a_y = y + a;
    adj_z = (a_y * 100) / a_x;
  }
  cout << a+1 << endl;

  return 0;
}
