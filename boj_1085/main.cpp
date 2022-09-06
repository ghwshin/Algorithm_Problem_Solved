#include <iostream>

using namespace std;

int main() {
  int x, y, w, h;
  cin >> x >> y >> w >> h;
  int mx, my;
  if (w - x > x) {
    mx = x;
  }
  else
    mx = w - x;
  if (h - y > y) {
    my = y;
  }
  else
    my = h - y;
  cout << ((mx > my) ? my : mx);
  return 0;
}
