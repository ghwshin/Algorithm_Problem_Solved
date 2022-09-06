#include <iostream>

using namespace std;

int main() {
  int n, nums[2];
  cin >> n;
  nums[0] = n / 5;
  while (nums[0] >= 0) {
    nums[1] = (n - nums[0] * 5) / 3;
    if (3 * nums[1] == (n - nums[0] * 5)){
      cout << nums[0] + nums[1];
      break;
    }
    nums[0]--;
  }
  if (3 * nums[1] != (n - nums[0] * 5))
    cout << -1;
  return 0;
}
