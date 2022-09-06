#include <iostream>

using namespace std;

int main() {
  int a, b, cnt = 0, current = 1, sum = 0;
  cin >> a >> b;
  for (int i = 1 ; i <= b ; i++) {
    cnt += 1;
    if (i >= a)
      sum += current;
    if (cnt == current) {
      cnt = 0;
      current += 1;
    }
  }
  cout << sum;
  return 0;
}
