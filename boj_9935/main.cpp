#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <stack>

using namespace std;

int main() {
  cin.tie();
  string in, ex;
  cin >> in;
  cin >> ex;
  deque<char> d;
  vector<char> vaild(ex.size());
  int idx = 0;
  for (int i = 0 ; i < in.size() ; i++) {
    d.push_back(in[i]);
    vaild[idx] = in[i];
    for (int j = 0 ; j < ex.size() ; j++) {

    }

  }

  return 0;
}
