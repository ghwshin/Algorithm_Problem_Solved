#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  long n;
  int number;
  cin.tie(NULL);
  cin.sync_with_stdio(false);
  cin >> number;
  vector<long> divided = vector<long>(number);
  if (number == 1) {
    cin >> divided[0];
    cout << divided[0] * divided[0];
  }
  else {
    for (int i = 0 ; i < number ; i++)
      cin >> divided[i];
    sort(divided.begin(),divided.end());
    cout << divided[0] * divided[divided.size() - 1];
  }
  return 0;
}
