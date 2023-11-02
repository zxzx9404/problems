/*
마을의 위성사진을 본 철수는 평지와 호수로 나뉘어져 있다는 것을 알았다.
이 사진을 통해 호수가 몇 개가 있는지 파악하려고 한다.
 상, 하, 좌, 우, 대각선 중 하나라도 연결되어 있으면 하나의 호수로 간주한다면 철수의 마을에 몇 개의 호수가 있는지 파악할 수 있는 프로그램을 작성하자.

첫째 줄에는 마을의 크기 N이 주어진다. (4<=N<=100)
둘째 줄부터 N줄까지 마을 정보가 공백 없이 주어진다.
(0은 평지 1은 호수임)

호수의 개수를 출력한다.

input
5
01010
10001
01010
00100
10000

output
2
*/


#include <iostream>
#include <queue>
using namespace std;

#define MAXN (100)
int N;
char map[MAXN+10][MAXN+10];
int visited[MAXN+10][MAXN+10];
int ans;
int di[8] = {0, 0, -1, 1, -1, -1, 1, 1};
int dj[8] = {-1, 1, 0, 0, -1, 1, 1, -1};

void InputData(){
	cin >> N;
	for (int i=0; i<N; i++){
		cin >> &map[i][0];
	}
}

void findLake(int sti, int stj) {
	queue<pair<int, int>> q;
	
	q.push(make_pair(sti, stj));
	visited[sti][stj] = 1;

	while (!q.empty()) {
		int i = q.front().first;
		int j = q.front().second;
		q.pop();

		for (int k=0; k<8; k++) {
			int ni = i + di[k];
			int nj = j + dj[k];

			if (0 <= ni && ni < N && 0 <= nj && nj < N && map[ni][nj] == '1' && !visited[ni][nj]) {
				visited[ni][nj] = 1;
				q.push(make_pair(ni, nj));
			}
		}
	}
}

void Solve() {
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			if (!visited[i][j] && map[i][j] == '1') {
				findLake(i, j);
				ans++;
			}
		}
	}

	cout << ans << endl;

}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();//입력
	//여기서부터 작성
	fill(&visited[0][0], &visited[MAXN+9][MAXN+10], 0);
	Solve();
	return 0;
}
