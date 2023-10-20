#include <iostream>
#include <vector>
#include <deque>
using namespace std;

#define MAXN (100)
int W, H; // 가로, 세로 크기
int sw, sh, ew, eh; // 출발 가로세로, 도착 가로세로 좌표
char map[MAXN + 10][MAXN + 10]; // 지도정보

void InputData() {
    cin >> W >> H;
    cin >> sw >> sh >> ew >> eh;
    for (int i = 1; i <= H; i++) {
        cin >> &map[i][1];
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int ans = -1;
    InputData(); // 입력

    vector<vector<int>> visited(H + 1, vector<int>(W + 1, 0));

    int dx[4]= {0, 0, -1, 1};
    int dy[4]= {1, -1, 0, 0};

    deque<pair<int, int>> arr;
    arr.push_back(make_pair(sh, sw));

    while (!arr.empty()) {
        int i = arr.front().first;
        int j = arr.front().second;
        arr.pop_front();

        for (int k = 0; k < 4; k++) {
            int ni = i + dy[k];
            int nj = j + dx[k];

            if (ni >= 1 && ni <= H && nj >= 1 && nj <= W && map[ni][nj]== '0' && visited[ni][nj]== 0) {
                visited[ni][nj]= visited[i][j]+ 1;
                arr.push_back(make_pair(ni, nj));
            }
        }
    }

    ans = visited[eh][ew];

    cout << ans << "\n"; // 출력
    return 0;
}
