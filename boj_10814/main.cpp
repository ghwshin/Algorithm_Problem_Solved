#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class na {
 public:
  int age;
  string name;

  bool operator<(const na& b) const {
    return this->age < b.age;
  }
};

int main() {
  cin.tie(NULL);
  cin.sync_with_stdio(false);
  int n;
  cin >> n;
  vector<na> jdata;
  jdata.resize(n);
  for(int i = 0 ; i < n ; i++) {
    cin >> jdata[i].age >> jdata[i].name;
  }
  stable_sort(jdata.begin(), jdata.end());
  for(auto tmp : jdata)
    cout << tmp.age << " " << tmp.name << "\n";
  return 0;
}
