#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n, tmp, t_cnt = 0;
  cin >> n;
  int current = 666;
  while (true) {
    tmp = current;
    while (tmp != 0) {
      if (tmp >= 100 and tmp % 10 == 6 and tmp % 100 == 6 and tmp % 1000 == 6) {
        t_cnt += 1;
        break;
      }
      tmp /= 10;
    }
    if (t_cnt == n) {
      cout << current << endl;
      break;
    }
    current += 1;
  }
  return 0;
}
