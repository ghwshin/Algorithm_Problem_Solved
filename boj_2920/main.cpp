#include <iostream>

using namespace std;

int main() {
  string a;
  int n[8] = {0, };
  for (int i = 0 ; i < 8 ; i++) {
    cin >> n[i];
    if (i == 0 and n[i] == 1)
      a = "ascending";
    else if (i == 0 and n[i] == 8)
      a = "descending";
    else if (i == 0)
      a = "mixed";
    else {
      if (a == "ascending" and n[i] != n[i - 1] + 1)
        a = "mixed";
      else if (a == "descending" and n[i] != n[i - 1] - 1)
        a = "mixed";
      else ;
    }
  }
  cout << a;
  return 0;
}
