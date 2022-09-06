#include <iostream>
#include <vector>

using namespace std;

vector<int> counts(10001, 0);

int main() {
  cin.tie(NULL);
  cin.sync_with_stdio(false);
  int n, tmp;
  cin >> n;
  for (int i = 0 ; i < n ; i++) {
    cin >> tmp;
    counts[tmp] += 1;
  }
  for (int i = 1 ; i <= 10001 ; i++) {
    for (int j = 0 ; j < counts[i] ; j++)
      cout << i << "\n";
  }
  return 0;
}
