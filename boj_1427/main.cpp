#include <iostream>
#include <string>

using namespace std;

int main() {
  string a;
  cin >> a;
  int maxidx;
  for (int i = 0 ; i < a.size() ; i++) {
    maxidx = i;
    for (int j = i ; j < a.size() ; j++) {
      if (a[maxidx] < a[j])
        maxidx = j;
    }
    if (maxidx != i) {
      char tmp = a[maxidx];
      a[maxidx] = a[i];
      a[i] = tmp;
    }
  }
  cout << a;
  return 0;
}
