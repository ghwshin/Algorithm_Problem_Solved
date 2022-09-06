#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int n, r = 0;
  cin >> n;
  vector<int> a = vector<int>(n);
  vector<int> b = vector<int>(n);
  for (int i = 0 ; i < n ; i++)
    cin >> a[i];
  for (int i = 0 ; i < n ; i++)
    cin >> b[i];
  sort(a.begin(), a.end());
  sort(b.begin(), b.end(), greater<int>());
  for (int i = 0 ; i < n ; i++)
    r += a[i] * b[i];
  cout << r;
  return 0;
}
