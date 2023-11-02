/*
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지 내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

input
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

output
3
7
8
9
*/


#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

#define MAXN (25)
int N;
char map[MAXN+10][MAXN+10];
int visited[MAXN+10][MAXN+10];
vector<int> ans;
int di[4] = {0, 0, -1, 1};
int dj[4] = {-1, 1, 0, 0};

void InputData(){
	cin >> N;
	for (int i=0; i<N; i++){
		cin >> &map[i][0];
	}
}

int findApt(int sti, int stj) {
	int cnt = 1;
	queue<pair<int, int>> q;
	
	q.push(make_pair(sti, stj));
	visited[sti][stj] = 1;

	while (!q.empty()) {
		int i = q.front().first;
		int j = q.front().second;
		q.pop();

		for (int k=0; k<4; k++) {
			int ni = i + di[k];
			int nj = j + dj[k];

			if (0 <= ni && ni < N && 0 <= nj && nj < N && map[ni][nj] == '1' && !visited[ni][nj]) {
				cnt++;
				visited[ni][nj] = 1;
				q.push(make_pair(ni, nj));
			}
		}
	}
	return cnt;
}

void Solve() {
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			if (!visited[i][j] && map[i][j] == '1') {
				int cnt = findApt(i, j);
				ans.push_back(cnt);
			}
		}
	}

	sort(ans.begin(), ans.end());
	cout << ans.size() << endl;
	for (int i=0; i<ans.size(); i++) {
		cout << ans[i] << endl;
	}
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
