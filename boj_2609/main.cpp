#include <iostream>

using namespace std;

int gcd(int a, int b) {
  int mod = a % b;
  if (mod == 0)
    return b;
  else
    return gcd(b, mod);
}

int main() {
  int a, b, r;
  cin >> a >> b;
  r = gcd(a, b);
  cout << r << "\n" << (a * b) / r;
  return 0;
}
