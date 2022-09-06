#include <iostream>

using namespace std;

int main() {
  int n, cnt = 0;
  cin >> n;
  if (n < 10)
    n = n*10;
  int t = n;
  do {
    int f = t % 10;
    int s = t / 10;
    int sum = f + s;
    t = f * 10 + (sum < 10 ? sum : sum % 10);
    cnt += 1;
  } while (n != t);
  cout << cnt << endl;
  return 0;
}
