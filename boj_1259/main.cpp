#include <iostream>
#include <vector>

using namespace std;

bool pelindrome(string a) {
  bool r = false;
  int s = a.size() - 1;
  if (s == 0)
    return true;
  for (int i = 0 ; i < a.size() ; i++) {
    if (i >= (s - i))
      break;
    if (a[i] == a[s - i])
      r = true;
    else {
      r = false;
      break;
    }
  }
  return r;
}

int main() {
  string a;
  while (true) {
    cin >> a;
    if (a == "0")
      break;
    else
      pelindrome(a) ? cout << "yes\n" : cout << "no\n";
  }
  return 0;
}
