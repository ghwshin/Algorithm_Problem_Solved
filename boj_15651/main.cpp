#include <iostream>
#include <vector>
#include <list>

using namespace std;

void dfs(int depth, int maxDepth, int n, vector<int>& number_arr, list<int>& result_arr);

int main() {
  int n, m, i;
  cin >> n >> m;
  vector<int> number_arr(n);
  list<int> result_arr;
  for (i = 0 ; i < n ; i++) {
    number_arr[i] = i + 1;
  }
  dfs(1, m, n, number_arr, result_arr);

  return 0;
}

void dfs(int depth, int maxDepth, int n, vector<int>& number_arr, list<int>& result_arr) {
  if (depth > maxDepth) {
    for (auto num : result_arr) {
      cout << num << " ";
    }
    cout << "\n";
    return;
  }
  for (int i = 0 ; i < n ; i++) {
    result_arr.push_back(i + 1);
    dfs(depth + 1, maxDepth, n, number_arr, result_arr);
    result_arr.pop_back();
  }
}