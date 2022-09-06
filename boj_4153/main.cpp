#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  vector<long long> a(3);
  while (true) {
    cin >> a[0] >> a[1] >> a[2];
    sort(a.begin(), a.end());
    if (a[0] == 0 and a[1] == 0 and a[2] == 0)
      break;
    if (a[0] * a[0] + a[1] * a[1] == a[2] * a[2])
      cout << "right\n";
    else
      cout << "wrong\n";
  }
  return 0;
}
