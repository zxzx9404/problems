/*
영희는 자외선이 피부에 좋지 않기 때문에 이동 시 자외선에 노출되는 것을 최소한으로 하고 싶어서 가는 길의 자외선 양을 모두 조사하였다.
값이 제 각각이어서 어떤 경로로 가야 좋을지 난감한 영희를 도와주자.
N*N 모양의 장소의 모든 길의 자외선 양이 주어지고 영희는 상하좌우 한 칸씩만 이동이 가능하다.
시작점(1,1)에서 도착점(N,N)까지 이동 시 자외선 합의 최소값을 찾아라.
예를 들어 3*3 장소의 자외선 양이 아래와 같다면 오른쪽처럼 이동하면 8만큼만 노출된다.

input
3
041
253
620

output
8
*/

#include <iostream>
#include <queue>
using namespace std;
#define MAXN (100)
int N;//가로, 세로 크기
char map[MAXN+10][MAXN+10];//지도정보
 
#define INF (1<<30)
int visited[MAXN+10][MAXN+10];
struct QUE{
    int r, c;
};
queue <QUE> que;
 
int BFS(){
    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};
    for (int i=1; i<=N; i++){
        for (int j=1; j<=N; j++){
            visited[i][j]=INF;
        }
    }
    que = {};
    que.push({1, 1});
    visited[1][1]=0;
    while(!que.empty()){
        QUE cur = que.front(); que.pop();
        for (int i=0; i<4; i++){
            int nr = cur.r+dr[i];
            int nc = cur.c+dc[i];
            if (map[nr][nc] == 0) continue;
            int ncost = visited[cur.r][cur.c] + map[nr][nc] - '0';
            if (visited[nr][nc] <= ncost) continue;
            que.push({nr, nc});
            visited[nr][nc] = ncost;
        }
    }
    return visited[N][N];
}
 
void InputData(){
    cin >> N;
    for (int i=1; i<=N; i++){
        cin >> &map[i][1];
    }
}
 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int ans = -1;
    InputData();//입력
 
    ans = BFS();//여기서부터 작성
 
    cout << ans << "\n";//출력
    return 0;
}
