#include <iostream>

using namespace std;

int main() {
  int x, bit, cnt = 0;
  cin >> x;
  while (x != 0) {
    if (x % 2 == 1)
      cnt++;
    x = x >> 1;
  }
  cout << cnt << endl;
  return 0;
}
