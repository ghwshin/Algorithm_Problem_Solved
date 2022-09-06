#include <iostream>
#include <deque>

using namespace std;

int main() {
  int n,t;
  cin >> n;
  deque<int> q;
  for (int i = 1 ; i <= n ; i++)
    q.push_back(i);
  while (q.size() > 1) {
    q.pop_front();
    t = q.front();
    q.pop_front();
    q.push_back(t);
  }
  cout << q.front();
  return 0;
}
