#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int n;
  cin >> n;
  pair<int, int> p;
  vector<pair<int, int>> ps(n);
  for (int i = 0 ; i < n ; i++) {
    cin >> p.first >> p.second;
    ps[i] = p;
  }
  sort(ps.begin(), ps.end());
  for (int i = 0 ; i < n ; i++)
    cout << ps[i].first << " " << ps[i].second << "\n";
  return 0;
}
