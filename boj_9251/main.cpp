#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
  string a, b;
  cin >> a >> b;
  int dp[b.size() + 1][a.size() + 1];

  for (int i = 0 ; i < b.size() + 1 ; i++) {
    for (int j = 0 ; j < a.size() + 1 ; j++) {
      if (i == 0 or j == 0)
        dp[i][j] = 0;
      else if (a[j - 1] == b[i - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
      }
      else {
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }
  cout << dp[b.size()][a.size()];
  return 0;
}
