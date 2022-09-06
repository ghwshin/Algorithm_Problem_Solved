#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(const pair<int, int> &a, const pair<int, int> &b) {
  if (a.second > b.second) {
    return false;
  }
  else if (a.second == b.second) {
    if (a.first > b.first)
      return false;
    else
      return true;
  }
  else
    return true;
}

int main() {
  cin.tie(NULL);
  cin.sync_with_stdio(false);
  int n;
  cin >> n;
  vector<pair<int, int>> p(n);
  for (int i = 0 ; i < n ; i++)
    cin >> p[i].first >> p[i].second;
  sort(p.begin(), p.end(), cmp);
  for (auto tmp : p)
    cout << tmp.first << " " << tmp.second << "\n";
  return 0;
}
