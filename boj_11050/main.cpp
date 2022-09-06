#include <iostream>

using namespace std;


int main() {
  int n, k;
  long long u = 1, d = 1;
  cin >> n >> k;
  if (n - k > k)
    k = n - k;
  for (int i = n ; i >= (n - k + 1); i--) {
    u = u * i;
  }
  for (int i = k ; i >= 2 ; i--)
    d = d * i;
  cout << u / d;
  return 0;
}
