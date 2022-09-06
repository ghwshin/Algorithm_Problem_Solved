#include <iostream>
#include <vector>
#include <string>

using namespace std;

void print_re(int _a, int _b, int _c, long long _re);

int main() {
  int a, b, c, i, j, k;
  long long dp[51][51][51];
  for (i = 0 ; i < 21 ; i++) {
    for (j = 0 ; j < 21 ; j++) {
      for (k = 0 ; k < 21 ; k++) {
        if (i == 0 or j == 0 or k == 0) {
          dp[i][j][k] = 1;
        }
        else if (i > 20 or j > 20 or k > 20) {
          dp[i][j][k] = dp[20][20][20];
        }
        else if (i < j and j < k) {
          dp[i][j][k] = dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][k];
        }
        else {
          dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1];
        }
      }
    }
  }

  while (true) {
    cin >> a >> b >> c;
    if (a == -1 and b == -1 and c == -1) {
      break;
    }
    else if (a <= 0 or b <= 0 or c <= 0) {
      print_re(a, b, c, 1);
    }
    else if (a > 20 or b > 20 or c > 20) {
      print_re(a, b, c, dp[20][20][20]);
    }
    else {
      print_re(a, b, c, dp[a][b][c]);
    }
  }

  return 0;
}

void print_re(int _a, int _b, int _c, long long _re) {
  cout << "w(" + to_string(_a) + ", " + to_string(_b) + ", " + to_string(_c) + ") = " + to_string(_re) + "\n";
}