#include <iostream>
using namespace std;

int main() {
  int re = 0, n;
  for (int i = 0 ; i < 5 ; i++) {
    cin >> n;
    re += n * n;
  }
  cout << re % 10;
  return 0;
}
