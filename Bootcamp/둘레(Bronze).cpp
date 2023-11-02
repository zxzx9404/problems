/*
농부 존은 그의 들판에 N(1≤N≤10,000)개의 건초 더미를 놓으려 한다. 
들판은 1*1 크기의 사각형으로 구성된 100*100 크기이고, 건초 더미들은 각각 1*1 크기의 사각형 한 칸을 차지한다. (한 칸에 두 개의 건초 더미가 놓이는 일은 없다)
 
농부 존은 건초 더미로 연결된 다양한 형태의 하나의 큰 영역이 생기는 것을 알았다. 
즉, 건초 더미들 모두 인접한 (동서남북으로 한 칸) 곳에 다른 건초 더미가 있다. 한 건초 더미에서 출발해서 다른 모든 건초 더미에 도달할 수 있다. 
건초 더미로 연결된 영역은 “구멍”을 포함할수있다. 구멍은 건초 더미로 완전히 둘러싸인 빈 영역이다.
 
농부 존이 건초 베일에 의해 형성되는 영역의 둘레를 계산하는 것을 도와주시오. “구멍”은 둘레에 영향을 주지 않는다.

input
8
5 3
5 4
8 4
5 5
6 3
7 3
7 4
6 5

output
14
*/


#include <iostream>
#include <string.h>
using namespace std;
#define MAXN ((int)1e4)
int N;
int X[MAXN+10];
int Y[MAXN+10];
 
int map[100+10][100+10];
int SH, SW, EH, EW;
int len;
int dh[] = {-1, 1, 0, 0};
int dw[] = {0, 0, -1, 1};
void FloodFill(int h, int w){
    if ((h<SH)||(h>EH)||(w<SW)||(w>EW)) return;//범위 벗어남
    if (map[h][w]==1){//둘레
        len++;
        return;
    }
    if (map[h][w] != 0) return;
    map[h][w]=2;
    for (int i=0; i<4; i++){
        FloodFill(h+dh[i], w+dw[i]);
    }
}
int Solve(){
    //0.초기화
    memset(map, 0, sizeof(map));
    //1.map 배열 건초더미 표시
    SH = SW = 100;
    EH = EW = 0;
    for (int i=0; i<N; i++){
        map[Y[i]][X[i]]=1;
        if (SH > Y[i]) SH = Y[i];//세로 하한
        if (SW > X[i]) SW = X[i];//가로 하한
        if (EH < Y[i]) EH = Y[i];//세로 상한
        if (EW < X[i]) EW = X[i];//가로 상한
    }
    SH--; SW--; EH++; EW++;
    //2.둘레 구하기
    len = 0;
    FloodFill(SH, SW);
    return len;
}
 
void InputData(){
    cin >> N;
    for (int i=0 ; i<N ; i++){
        cin >> X[i] >> Y[i];
    }
}
 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int ans = -1;
    InputData();// 입력받는 부분
 
    ans = Solve();// 여기서부터 작성
 
    cout << ans << "\n";// 출력하는 부분
    return 0;
}
