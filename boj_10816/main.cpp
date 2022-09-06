#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  cin.tie(NULL);
  cin.sync_with_stdio(false);
  int n, m, t;
  cin >> n;
  vector<int> ns(n);
  for (int i = 0 ; i < n ; i++)
    cin >> ns[i];
  sort(ns.begin(), ns.end());
  cin >> m;
  for (int i = 0 ; i < m ; i++) {
    cin >> t;
    cout << upper_bound(ns.begin(), ns.end(), t) - lower_bound(ns.begin(), ns.end(), t) <<  " ";
  }
  return 0;
}
