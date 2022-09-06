#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  cin.tie(NULL);
  cin.sync_with_stdio(false);
  int n;
  cin >> n;
  vector<int> a(n);
  for (int i = 0 ; i < n ; i++)
    cin >> a[i];
  sort(a.begin(),a.end());
  int avg, mid, fre_n = 0, sum = 0, ran;
  vector<int> fre;
  mid = a[n / 2];
  ran = a[a.size() - 1] - a[0];
  for (int i = 0 ; i < n ; i++) {
    sum += a[i];
    auto b = upper_bound(a.begin(), a.end(), a[i]) - lower_bound(a.begin(), a.end(), a[i]);
    if (b > fre_n) {
      fre_n = b;
      fre.clear();
      fre.push_back(a[i]);
    }
    else if (b == fre_n) {
      fre.push_back(a[i]);
    }
    else ;
  }
  fre.erase(unique(fre.begin(), fre.end()), fre.end());
  sort(fre.begin(), fre.end());
  avg = (int)((float)sum * 10 / n);
  if (avg > 0) {
    if ((avg % 10) >= 5)
      avg = avg / 10 + 1;
    else
      avg = avg / 10;
  }
  else {
    if ((avg % 10) <= -5)
      avg = avg / 10 - 1;
    else
      avg = avg / 10;
  }
  cout << avg << "\n" << mid << "\n" << ((fre.size() == 1) ? fre[0] : fre[1]) << "\n" << ran;
  return 0;
}
