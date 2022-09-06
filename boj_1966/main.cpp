#include <iostream>
#include <queue>

using namespace std;

struct comp {
  bool operator() (pair<int, int>& a, pair<int, int>& b) {
    if (a.first == b.first) {
      return a.second <= b.second;
    }
    return a.first < b.first;
  }
};

int main() {
  cin.tie(NULL);
  cin.sync_with_stdio(false);
  int tc, n, m, i, t;
  cin >> tc;
  for (i = 0 ; i < tc ; i++) {
    cin >> n >> m;
    priority_queue<pair<int, int>, vector<pair<int, int>>, comp> pq;
    for (int j = 0 ; j < n ; j++) {
      cin >> t;
      pq.push(pair<int, int>(t, j));
    }
    int cnt = 1;
    while (pq.top().second != m) {
      cnt += 1;
      pq.pop();
    }
    cout << cnt << "\n";
  }
  return 0;
}
