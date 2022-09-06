#include <iostream>
#include <deque>

using namespace std;

int main() {
  int n, v;
  cin >> n;
  deque<int> q;
  string c;
  for (int i = 0 ; i < n ; i++) {
    cin >> c;
    if (c == "push_front") {
      cin >> v;
      q.push_front(v);
    }
    else if (c == "push_back") {
      cin >> v;
      q.push_back(v);
    }
    else if (c == "pop_front") {
      if (q.empty())
        cout << "-1" << "\n";
      else {
        cout << q.front() << "\n";
        q.pop_front();
      }
    }
    else if (c == "pop_back") {
      if (q.empty())
        cout << "-1" << "\n";
      else {
        cout << q.back() << "\n";
        q.pop_back();
      }
    }
    else if (c == "size") {
      cout << q.size() << "\n";
    }
    else if (c == "empty") {
      cout << q.empty() << "\n";
    }
    else if (c == "front") {
      if (q.empty())
        cout << "-1" << "\n";
      else
        cout << q.front() << "\n";
    }
    else if (c == "back") {
      if (q.empty())
        cout << "-1" << "\n";
      else
        cout << q.back() << "\n";
    }
    else ;
  }
  return 0;
}
