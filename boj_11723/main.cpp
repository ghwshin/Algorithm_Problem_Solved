#include <iostream>

using namespace std;

class set {
  unsigned int s = 0;
 public:
  void add(int x) {
    s = s | (1 << x);
  }
  void remove(int x) {
    if (check(x) == 1)
      s = s ^ (1 << x);
  }
  int check(int x) {
    if ((s | (1 << x)) == s)
      return 1;
    else
      return 0;
  }
  void toggle(int x) {
    if (check(x) == 1)
      remove(x);
    else
      add(x);
  }
  void all() {
    s = s | 2097150;
  }
  void clear() {
    s = 0;
  }
};

int main() {
  cin.tie(NULL);
  cin.sync_with_stdio(false);
  int n;
  cin >> n;
  string tmp;
  set s = set();
  int x;
  for (int i = 0 ; i < n ; i++) {
    cin >> tmp;
    if (tmp.substr(0, 2) == "ad") {
      cin >> x;
      s.add(x);
    }
    else if (tmp.substr(0,2) == "re") {
      cin >> x;
      s.remove(x);
    }
    else if (tmp.substr(0,2) == "ch") {
      cin >> x;
      cout << s.check(x) << "\n";
    }
    else if (tmp.substr(0,2) == "to") {
      cin >> x;
      s.toggle(x);
    }
    else if (tmp.substr(0,2) == "em") {
      s.clear();
    }
    else if (tmp.substr(0,2) == "al") {
      s.all();
    }
  }

  return 0;
}
