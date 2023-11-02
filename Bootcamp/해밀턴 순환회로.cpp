/*
문제를 잘 풀기로 소문난 도경이는 모든 올림피아드 대회에 참가하고 싶어 했다. 대회에 참가하여 상이란 상은 다 타고 싶은 마음이었지만, 한 가지 걸리는 것이 있었다.
문제는 올림피아드 대회가 모두 해외에서 열리는 관계로 비행기 값이 굉장히 많이 들어간다는 것이다. 
결국에는 집으로 다시 돌아와야 하는데, 모든 대회에 1번씩만 참가하고 집으로 돌아오는 경비를 가장 최소화하고 싶다. 
도경이는 이것을 해결하지 못하면, 대회에 참가하기가 어렵게 된다. 대회는 참가하기만 하면 언제든지 알고리즘 문제를 풀 수 있기 때문에 경비를 계산하는 것 이외의 사항은 고려하지 않아도 된다.

첫 줄은 참가하는 대회의 수 N(1≤N≤12)을 입력 받는다. 이때, 출발지(집)는 1번으로 한다.
둘째 줄은 N*N 크기의 대회 개최지와 개최지를 이동하는 항공료(0≤항공료<100)가 나온다. 각 항공료는 한 칸의 공백으로 구분된다. 
만약에 개최지에서 개최지로 이동할 수 있는 항공로가 없다면 항공료의 값을 0으로 표시한다.
집에서 출발하여 전체 대회를 모두 참가하고 돌아올 때, 최소의 항공료를 출력한다.

input
5
0 14 4 10 20 
14 0 7 8 7 
4 5 0 7 16 
11 7 9 0 2 
18 7 17 4 0 

output
30

예제의 비용 (경로)
10 (1->4)
+ 2 (4->5)
+ 7 (5->2)
+ 7 (2->3)
+ 4 (3->1)
= 30
*/


#include <iostream>
using namespace std;
#define MAXN (12)
int N;//대회수
int A[MAXN+10][MAXN+10];//[출발][도착]=항공료
 
#define INF (1<<30)
bool used[MAXN + 10];
int sol;
void DFS(int s, int n, int sum){
    int e;
    if (sol <= sum) return;
    if (n >= N){//종료조건
        if (A[s][1] != 0){//마지막 도시에서 출발도시(1)에 갈수있어야 함
            if (sol > sum + A[s][1]) sol = sum + A[s][1];
        }
        return;
    }
    for (e = 2; e <= N; e++){
        if (A[s][e] == 0) continue;//경로없음
        if (used[e]) continue;
        used[e] = true;
        DFS(e, n+1, sum+A[s][e]);
        used[e] = false;
    }
}
int Solve(){
    sol = INF;
    DFS(1, 1, 0);//출발도시, 들린도시수, 총비용
    return sol;
}
 
void InputData(){
    cin >> N;
    for (int i=1; i<=N; i++){
        for (int j=1; j<=N; j++){
            cin >> A[i][j];
        }
    }
}
 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int ans = -1;
    InputData();//입력
 
    ans = Solve();//여기서부터 작성
 
    cout << ans << "\n";//출력
    return 0;
}
