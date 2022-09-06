#include <iostream>
#include <utility>
#include <vector>
#include <queue>
#include <sstream>

using namespace std;

class AC {
  string p;
  int n;
  deque<int> dq;
 public:
  void split(string &str, char delimiter) {
    istringstream iss(str);
    int i;
    string buffer;
    while (getline(iss, buffer, delimiter)) {
      stringstream sint(buffer);
      sint >> i;
      dq.push_back(i);
    }
  }
  void setting(string _p, int _n) {
    p = std::move(_p);
    n = _n;
  }
  void addqueue() {
    string arr;
    cin >> arr;
    arr = arr.substr(1, arr.size() - 2);
    split(arr, ',');
  }
  void getresult() {
    bool isrevert = false;
    for (auto t : p) {
      if (t == 'R') {
        isrevert = !isrevert;
      }
      else {
        if (dq.empty()) {
          cout << "error" << "\n";
          return;
        }
        if (isrevert)
          dq.pop_back();
        else
          dq.pop_front();
      }
    }
    cout << "[";
    if (dq.empty()) {
      cout << "]\n";
    }
    else {
      if (!isrevert) {
        while (dq.size() != 1) {
          cout << dq.front() << ",";
          dq.pop_front();
        }
        cout << dq.front() << "]\n";
        dq.pop_front();
      }
      else {
        while (dq.size() != 1) {
          cout << dq.back() << ",";
          dq.pop_back();
        }
        cout << dq.back() << "]\n";
        dq.pop_back();
      }
    }
  }
};

int main() {
  cin.tie(NULL);
  cin.sync_with_stdio(false);
  int t;
  cin >> t;
  string tmpp;
  int tmp;
  AC q = AC();
  for (int i = 0 ; i < t ; i++) {
    cin >> tmpp;
    cin >> tmp;
    q.setting(tmpp, tmp);
    q.addqueue();
    q.getresult();
  }
  return 0;
}
