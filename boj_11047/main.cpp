#include <iostream>
#include <vector>

using namespace std;

int main() {
  int tmp, n, k, i, coin_n = 0 ,c_max = 0;
  cin >> n >> k;
  vector<int> coins;
  for (i = 0 ; i < n ; i++) {
    cin >> tmp;
    coins.push_back(tmp);
  }
  int idx = coins.size() - 1;
  while (true) {
    c_max += coins[idx];
    coin_n += 1;
    if (c_max == k) {
      break;
    }
    else if (c_max > k) {
      c_max -= coins[idx];
      coin_n -= 1;
      idx -= 1;
    }
    else ;
  }
  cout << coin_n;
  return 0;
}
