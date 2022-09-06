#include <iostream>
#include <stack>

using namespace std;

bool isvaild(string &a) {
  stack<char> p;
  if (a[0] == ')')
    return false;
  else {
    p.push(a[0]);
    for (int i = 1 ; i < a.size() ; i++) {
      if (a[i] == '(')
        p.push(a[i]);
      else {
        if (p.empty())
          return false;
        else
          p.pop();
      }
    }
  }
  if (p.empty())
    return true;
  else
    return false;
}

int main() {
  int n;
  cin >> n;
  string in;
  for (int i = 0 ; i < n ; i++) {
    cin >> in;
    cout << (isvaild(in) ? "YES" : "NO") << "\n";
  }
  return 0;
}
