/*
보물섬 지도를 발견한 후크 선장은 보물을 찾아 나섰다. 보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 
각 칸은 육지(L)나 바다(W)로 표시되어 있다. 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다.
보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 
육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안된다.

WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
예를 들어 위와 같이 지도가 주어졌다면 보물은 (3, 0), (4, 1)에 묻혀 있게 되고, 이 둘 사이의 최단 거리로 이동하는 시간은 8시간이 된다.
보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.

input
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW

output
8
*/


#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
#define MAXN (50)
struct T{
    int i, j, cnt;
};
int di[4] = {0, 0, -1, 1};
int dj[4] = {-1, 1, 0, 0};
int H, W;//지도 세로, 가로 크기
char map[MAXN+10][MAXN+10];//지도정보(W:바다, L:육지)

void InputData(){
	cin >> H >> W;
	for (int i=0; i<H; i++){
		cin >> &map[i][0];
	}
}

int Solve(int si, int sj) {
    queue<T> q;
    q.push({si, sj, 0});
    int cnt = 0;
    int visited[MAXN+10][MAXN+10];
    visited[si][sj] = 1;
    fill(&visited[0][0], &visited[MAXN+9][MAXN+10], 0);

    while (!q.empty()) {
        T t = q.front();
        q.pop();

        if (cnt < t.cnt) {
            cnt = t.cnt;
        }

        for (int k=0; k<4; k++) {
            int ni, nj;
            ni = t.i + di[k];
            nj = t.j + dj[k];

            if (0 <= ni && ni < H && 0 <= nj && nj < W && map[ni][nj] == 'L' && !visited[ni][nj]) {
                q.push({ni, nj, t.cnt+1});
                visited[ni][nj] = 1;
            }
        }
    }

    return cnt;
}

int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int ans = -1;
	InputData();//입력받는 부분

	//여기서부터 작성
    for (int i=0; i<H; i++) {
        for (int j=0; j<W; j++) {
            if (map[i][j] == 'L') {
                int temp = Solve(i, j);
                if (temp > ans) {
                    ans = temp;
                }
            }
        }
    }
	cout << ans << "\n";//출력하는 부분
	return 0;
}
