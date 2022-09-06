#include <iostream>

using namespace std;

void print(int n) {
  if (n == 3) {
    cout << "***" << "\n" << "* *" << "\n" << "***";
    return;
  }
  for (int i = 0 ; i < 9 ; i++) {
    if (i == 4) {
      for (int j = 0 ; j < n / 3 ; j++) {
        for (int k = 0 ; k < n / 3 ; k++) {
          cout << " ";
        }
        cout << "\n";
      }
    }
    else {
      print(n / 3);
    }
    if ((i + 1) % 3 == 0)
      cout << "\n";
  }
}

int main() {
  int n;
  cin >> n;
  print(n);
  return 0;
}
