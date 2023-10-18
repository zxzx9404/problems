/*
컴퓨터 과학과 학생회의 유일한 프린터는 매우 무거운 작업량을 겪고 있다.
때로는 수백 개의 작업으로 인해 한 페이지 출력을 얻으려면 몇 시간을 기다려야 할 수 있다.
일부 작업이 다른 작업보다 중요하기 때문에 학생회의 회장인 철수는 대기 열에 대한 간단한 우선 순위 시스템을 발명하고 구현했다.
이제 각 작업에 우선 순위가 1과 9 사이(9가 가장 높은 우선 순위이고 1이 가장 낮음)에서 지정된다.
 
프린터는 다음과 같이 작동한다.
 
- 대기 열의 첫 번째 작업인 J를 대기 열에서 가져옴.
- 대기 열에 작업 J보다 우선 순위가 높은 작업이 있는 경우, J를 인쇄하지 않고 대기 열 끝으로 이동 시킴.
- 그렇지 않으면 작업 J를 인쇄 함 (다시 대기 열에 넣지 않음)
 
이러한 방식의 발명으로 우선순위가 높은 중요한 문서는 매우 빨리 인쇄되지만, 중요도가 낮은 다른 문서들은 인쇄되기까지 꽤 오래 기다려야 할 수 도 있다.
 
위 방법으로 프린터가 작동할 때, 현재 대기 열에 있는 문서의 수와 우선순위가 주어졌을 때, 어떤 한 문서가 몇 번째 순서로 인쇄되는지 출력하는 프로그램을 작성하자.

*/

#include <iostream>
#include <queue>
using namespace std;

#define MAXN (100)
int N, M;//문서수, 궁금한 문서 번호
int P[MAXN+10];//문서 우선순위
void InputData() {
    cin >> N >> M;
    for (int i=0; i<N; i++){
        cin >> P[i];
    }
}


int Solve(void) {
    int cnt = 0;
    int NumCnt[10] = {0};
    queue<pair<int, int>> Q;

    for (int i=0; i<N; i++) {
        NumCnt[P[i]]++;
        Q.push(make_pair(P[i], i));
    }

    while (true) {
        pair<int, int> now = Q.front();
        Q.pop();

        for (int i=9; i >= now.first; i--) {
            if (i > now.first && NumCnt[i] > 0) {
                Q.push(now);
                break;
            }

            if (i == now.first) {
                cnt++;
                NumCnt[now.first]--;
                if (now.second == M) {
                    return cnt;
                }
            }
        }
    }
    
    return -1;
}

int main() {
    int ans = -1;
    int T;
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    cin >> T;
    for (int t=1; t<=T; t++){
        InputData();//입력받는 부분

        //여기서부터 작성
        ans = Solve();

        cout << ans << "\n";//출력하는 부분
    }
    return 0;
}
