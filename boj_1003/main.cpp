#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int n;
  cin >> n;
  vector<int> case_f(n);
  for (int i = 0 ; i < n ; i++) {
    int t;
    cin >> t;
    case_f[i] = t;
  }
  vector<long long> f_0(41, 0);
  vector<long long> f_1(41, 0);
  f_0[0] = 1;
  f_1[1] = 1;
  for (int i = 2 ; i < 41 ; i++) {
    f_0[i] = f_0[i - 1] + f_0[i - 2];
    f_1[i] = f_1[i - 1] + f_1[i - 2];
  }
  for (int i = 0 ; i < n ; i++) {
    cout << f_0[case_f[i]] << " " << f_1[case_f[i]] << "\n";
  }
  return 0;
}
