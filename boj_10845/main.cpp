#include <iostream>
#include <vector>

using namespace std;

class Vqueue {
 private:
  int max;
  int ptr;
  vector<int> data;

 public:
  Vqueue() : max(10000), ptr(0), data(vector<int>(max)) {}

  int push(int x) {
    if (max <= ptr)
      return -1;
    data[ptr++] = x;
    return 0;
  }

  int pop(void) {
    if (ptr <= 0)
      return -1;
    int tmp = data[0];
    for (int i = 0 ; i < ptr ; i++) {
      data[i] = data[i + 1];
    }
    ptr--;
    return tmp;
  }

  int size(void) {
    return ptr;
  }

  int empty(void) {
    return ptr == 0;
  }

  int front(void) {
    if (ptr <= 0)
      return -1;
    return data[0];
  }

  int back(void) {
    if (ptr <= 0)
      return -1;
    return data[ptr - 1];
  }
};

int main() {
  int n, p;
  string comd;
  cin >> n;
  Vqueue q = Vqueue();
  for (int i = 0 ; i < n ; i++) {
    cin >> comd;
    if (comd == "push") {
      cin >> p;
      q.push(p);
    }
    else if (comd == "pop") {
      cout << q.pop() << "\n";
    }
    else if (comd == "size") {
      cout << q.size() << "\n";
    }
    else if (comd == "empty") {
      cout << q.empty() << "\n";
    }
    else if (comd == "front") {
      cout << q.front() << "\n";
    }
    else if (comd == "back") {
      cout << q.back() << "\n";
    }
    else ;
  }
  return 0;
}
