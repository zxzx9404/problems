/*
(주)정올에서는 여러 개의 빌딩을 새로 지을 계획이다. 그래서 빌딩을 세울 장소를 선정하였다. 그리고 각 빌딩을 각 장소에 세울 경우에 드는 비용을 추정하였다. 예를 들어서 아래의 표를 보자
 
             1 2 3
           A 4 7 3
           B 2 6 1
           C 3 9 4
 
A, B, C 는 건물을 나타내고, 1, 2, 3은 장소를 나타낸다. 예를 들어서 건물 B를 장소 1에 세우면 비용이 2가 들고, 장소 2에 세우면 비용이 6, 장소 3에 세우면 비용이 1만큼 든다. 물론 한 장소에는 한 건물밖에 세울 수 없다. 만일 A를 장소 2에, B를 장소 3에, C를 1에 세우면 전체 비용이 7+1+3 = 11이 필요하다. 그런데 A를 3, B를 1, C를 2에 세우면 3+2+9 = 14 가 필요하다.
 
각 빌딩을 어느 장소에 세우면 비용의 합이 최소가 되는지 구하는 프로그램을 작성하시오.

입력 파일의 첫 줄은 빌딩의 개수 n(1≤n≤10)이 들어있다.
그 다음 n 줄에는 각 건물을 각 장소에 세울 경우에 드는 비용이 입력된다. 물론 각 줄 에는 n개의 수가 입력된다.
비용을 나타내는 수의 범위는 1이상 100미만이다.

input
4
11 12 18 40
14 15 13 22
11 17 19 23
17 14 20 28

output
61
*/


#include <iostream>
using namespace std;
#define MAXN (10)
int N;//빌딩개수(장소개수)
int A[MAXN+10][MAXN+10];//[빌딩][장소]=비용
int usingArr[MAXN+10] = {0};
int ans = 1000;

void InputData(){
	cin >> N;
	for (int i=0; i<N; i++){
		for (int j=0; j<N; j++){
			cin >> A[i][j];
		}
	}
}

void DFS(int cnt, int sum) {
	if (ans <= sum) return;
	if (cnt == N) {
		ans = sum;
		return;
	}
	for (int i=0; i<N; i++) {
		if (!usingArr[i]) {
			usingArr[i] = 1;
			DFS(cnt + 1, sum + A[cnt][i]);
			usingArr[i] = 0;
		}
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();//입력

	//여기서부터 작성
	DFS(0, 0);
	cout << ans << "\n";//출력
	return 0;
}
