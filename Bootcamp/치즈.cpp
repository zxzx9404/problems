// BOJ 2636 치즈와 동일 문제

#include <iostream>
#include <queue>
using namespace std;
#define MAXN (100)
int H, W;
int map[MAXN+10][MAXN+10];
int hour, sol, ex_sol;
int di[4] = {0, 0, -1, 1};
int dj[4] = {1, -1, 0, 0};
void InputData(){
	cin >> H >> W;
	for (int i=0; i<H; i++){
		for (int j=0; j<W; j++){
			cin >> map[i][j];
		}
	}
}

queue<pair<int, int>> BFS(queue<pair<int, int>> q) {

    queue<pair<int, int>> next_q;

    while (!q.empty()) {
        pair<int, int> t = q.front();
        q.pop();
        int i = t.first;
        int j = t.second;
        for (int k=0; k<4; k++) {
            int ni = i + di[k];
            int nj = j + dj[k];

            if (0 <= ni && ni < H && 0 <= nj && nj < W) {
                if (map[ni][nj] == 0) {
                    q.push({ni, nj});
                } else if (map[ni][nj] == 1) {
                    next_q.push({ni, nj});
                    sol++;
                }
                map[ni][nj] = -1;
            }
        }
    }

    return next_q;    
}

int Solve() {
    int hour = 0;
    queue<pair<int, int>> q;
    q.push({0, 0});
    map[0][0] = -1;

    queue<pair<int, int>> next_q = BFS(q);

    while (!next_q.empty()) {
        ex_sol = sol;
        sol = 0;
        next_q = BFS(next_q);
        hour++;
    };

    return hour;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();// 입력받는 부분

	// 여기서부터 작성
    hour = Solve();

	// 출력하는 부분
	cout << hour << "\n" << ex_sol << "\n";
	return 0;
}
