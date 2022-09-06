#include <iostream>
#include <vector>

using namespace std;

int main() {
  cin.tie(NULL);
  cin.sync_with_stdio(false);
  int n, m, t;
  cin >> n >> m;
  vector<int> c(n);
  for (int i = 0 ; i < n ; i++)
    cin >> c[i];

  int cur = 0;
  for (int i = 0 ; i < n ; i++) {
    int j = 0;
    while (true) {
      if (j == n)
        break;
      if (i != j) {
        int k = 0;
        while (true) {
          if (k == n)
            break;
          if (k != i and k != j) {
            t = c[i] + c[j] + c[k];
            if (cur < t and t <= m)
              cur = t;
          }
          k++;
        }
      }
      j++;
    }
    if (cur == m)
      break;
  }
  cout << cur;
  return 0;
}
