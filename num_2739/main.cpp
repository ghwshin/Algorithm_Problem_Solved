#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n,f,s;
  cin >> n;
  vector<int> r(n);
  for (int i = 0 ; i < n ; i++) {
    cin >> f >> s;
    r[i] = f + s;
  }
  for (int i = 0 ; i < n; i++)
    cout << r[i] << endl;
  return 0;
}
