#include <iostream>
#include <queue>

using namespace std;

int main() {
  cin.tie(NULL);
  cin.sync_with_stdio(false);
  int n, t;
  cin >> n;
  priority_queue<int, vector<int>, greater<int>> pq;
  for (int i = 0 ; i < n ; i++) {
    cin >> t;
    pq.push(t);
  }
  int sum = 0, psum = 0;
  while (!pq.empty()) {
    psum += pq.top();
    sum += psum;
    pq.pop();
  }
  cout << sum;
  return 0;
}
