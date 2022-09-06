#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct comp {
  bool operator()(const pair<string, string>& v, const string & k) {
    return (v.first < k);
  }
  bool operator()(const string & k, const pair<string, string>& v) {
    return (k < v.first);
  }
};


int main() {
  cin.tie();
  cin.sync_with_stdio(false);
  int n, m;
  cin >> n >> m;
  string add, tpass;
  vector<pair<string, string>> pass(n);
  for (int i = 0 ; i < n ; i++) {
    cin >> add >> tpass;
    pass[i] = pair<string, string>(add, tpass);
  }
  sort(pass.begin(), pass.end());
  for (int i = 0 ; i < m ; i++) {
    cin >> add;
    cout << pass[].second << "\n";
  }

  return 0;
}
