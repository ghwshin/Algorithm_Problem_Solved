#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
  int k, n;
  cin >> n >> k;
  queue<int> q, t;
  vector<int> re;
  for (int i = 1 ; i <= n ; i++)
    q.push(i);
  while (q.size() != 1) {
    if (q.size() >= k) {
      for (int j = 1 ; j <= k ; j++) {
        t.push(q.front());
        q.pop();
      }
    }
    else {
      int s = k % q.size() == 0 ? q.size() : k % q.size();
      for (int j = 1 ; j <= s ; j++) {
        t.push(q.front());
        q.pop();
      }
    }
    while (!t.empty()) {
      if (t.size() == 1) {
        re.push_back(t.front());
        t.pop();
      }
      else {
        q.push(t.front());
        t.pop();
      }
    }
  }
  re.push_back(q.front());
  cout << "<";
  for (int i = 0 ; i < n - 1 ; i++)
    cout << re[i] << ", ";
  cout << re[n - 1] << ">";

  return 0;
}
