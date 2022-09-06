#include <iostream>
#include <vector>

using namespace std;

class Grid {
 private:
  vector<int> rgb = vector<int>(3, 0);
  vector<int> dx = {-1, 1, 0 , 0};
  vector<int> dy = {0, 0, -1, 1};
  vector<string> grid;
  vector<vector<bool>> finded;
  int n;

 public:
  Grid(int _n){
    n = _n;
    grid = vector<string>(n);
    finded = vector<vector<bool>>(n, vector<bool>(n, false));
  }
  void makeGrid() {
    for (int i = 0 ; i < n ; i++) {
      string tmp;
      cin >> tmp;
      grid[i] = tmp;
    }
  }

  bool is_out(int row, int col) {
    return row < 0 or col < 0 or row >= n or col >= n;
  }

  void find_rgb_normal(int x, int y, char cur_color) {
    finded[x][y] = true;
    if (grid[x][y] == cur_color) {
      for (int i = 0 ; i < 4 ; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (!is_out(nx, ny) and grid[x][y] == cur_color) {
          find_rgb_normal(nx, ny, cur_color);
        }
      }
    }
  }

  void incre_rgb(char color) {
    if (color == 'R') {
      rgb[0]++;
    } else if (color == 'G') {
      rgb[1]++;
    } else {
      rgb[2]++;
    }
  }


};
int main() {
  cin.tie();
  cin.sync_with_stdio(false);
  int n, i, j;
  cin >> n;
  Grid grid = Grid(n);

  grid.makeGrid();
  for (i = 0 ; i < n ; i++) {
    for (j = 0 ; j < n ; j++) {
      if ()
    }
  }


  return 0;
}

void rgb_find(int n, int x, int y, vector<string>& grid, vector<vector<bool>>& finded, bool color) {
  finded[x][y] = true;

}
