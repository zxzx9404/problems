#include <iostream>
#include <queue>
using namespace std;
#define MAXN (100)
int N, M;//지하철역수, 목적역
int S[MAXN+2][MAXN+2];//[s][e]=시간
 
#define INF (1<<30)
int visited[MAXN+2];
int path[MAXN+2];
queue <int> que;
 
int BFS(){
    for (int i=1; i<=N; i++){
        visited[i] = INF;
        path[i] = 0;
    }
    que = {};
    que.push(1);
    visited[1]=0;
    path[1]=0;
    while (!que.empty()){
        int cur = que.front(); que.pop();
        for (int e=2; e<=N; e++){
            int ntime = visited[cur] + S[cur][e];
            if (visited[e] <= ntime) continue;
            que.push(e);
            visited[e] = ntime;
            path[e]=cur;
        }
    }
    return visited[M];
}
 
void PRT(int m){
    if (m == 0) return;
    PRT(path[m]);
    cout << m << " ";
}
void OutputData(int ans){
    cout << ans << "\n";
    PRT(M);
    cout << "\n";
}
 
void InputData(){
    cin >> N >> M;
    for (int s=1; s<=N; s++){
        for (int e=1; e<=N; e++){
            cin >> S[s][e];
        }
    }
}
 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    InputData();
    int ans = BFS();
    OutputData(ans);
    return 0;
}





/*
#include <iostream>
#include <vector>
using namespace std;
 
int N, M;
vector<vector<int>> metro;
int ans = 10000;
vector<int> visited;
vector<int> route;
 
void dfs(int now, int mins, const vector<int>& way) {
    if (mins > visited[now]) {
        return;
    }
 
    for (int i = 0; i < N; i++) {
        if (i != now && visited[i]> mins + metro[now][i]&& ans > mins + metro[now][i]) {
            visited[i]= mins + metro[now][i];
 
            if (i == M && ans > mins + metro[now][i]) {
                ans = mins + metro[now][i];
                route = way;
                route.push_back(M);
            } else {
                vector<int> newWay = way;
                newWay.push_back(i);
                dfs(i, mins + metro[now][i], newWay);
            }
        }
    }
}
 
int main() {
    cin >> N >> M;
    M -= 1;
    metro.resize(N, vector<int>(N));
    visited.resize(N, 10000);
 
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> metro[i][j];
        }
    }
 
    dfs(0, 0, vector<int>{0});
 
    cout << ans << endl;
    for (size_t i = 0; i < route.size(); i++) {
        cout << route[i]+ 1 << " ";
    }
 
    return 0;
}
*/
