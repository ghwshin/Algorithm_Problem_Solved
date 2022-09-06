#include <iostream>
#include <vector>

using namespace std;

int main() {
  cin.tie(nullptr);
  cin.sync_with_stdio(false);
  int n, t, cnt = 0;
  cin >> n;
  vector<int> prime(1001, 1);
  prime[1] = 0;
  for (int i = 2 ; i <= 1000 ; i++) {
    for (int j = i ; j < 1001 ; j = j + i) {
      if (j != i)
        prime[j] = 0;
    }
  }
  for (int i = 0 ; i < n ; i++) {
    cin >> t;
    if (prime[t] == 1)
      cnt++;
  }
  cout << cnt;
  return 0;
}
