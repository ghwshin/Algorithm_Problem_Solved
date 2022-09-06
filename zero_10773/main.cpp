#include <iostream>
#include <stack>

using namespace std;

int main() {
  int n, x;
  stack<int> stk;
  cin >> n;
  for(int i = 0 ; i < n ; i++) {
    cin >> x;
    if (x == 0)
      stk.pop();
    else
      stk.push(x);
  }
  long long result = 0;
  while (!stk.empty()) {
    result += stk.top();
    stk.pop();
  }
  cout << result << endl;
  return 0;
}
