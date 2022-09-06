#include <iostream>

using namespace std;

int cnt = 0;
int r, c;

void z(int x, int y, int n) {
  if (n == 0) {
    cout << cnt;
    return ;
  }
  if (x < n / 2 and y < n / 2)
    z(x, y, n / 2);
  else if (x < n / 2 and y >= n / 2) {
    cnt += (n / 2 * n / 2);
    z(x, y - n / 2, n / 2);
  }
  else if (x >= n / 2 and y < n / 2) {
    cnt += (n / 2 * n / 2) * 2;
    z(x - n / 2, y, n / 2);
  }
  else {
    cnt += (n / 2 * n / 2) * 3;
    z(x - n / 2, y - n / 2, n / 2);
  }
}

int main() {
  int n;
  cin >> n >> r >> c;
  z(r, c, 2 << (n - 1));
  return 0;
}
