/*
N장의 카드로 구성 된 카드 덱(Deck)이 있다. 이 카드는 1번 카드가 가장 위에, N번 카드가 가장 아래쪽에 있는 형태로 놓여져 있다. 이제 이 카드를 아래의 규칙에 따라서 수행하면서 한 장씩 상대방에게 전달할 것이다.
 
1) 가장 아래 카드 번호를 2로 나눈 몫의 정수만큼 반복하여 제일 위에 올라와 있는 카드부터 한 장씩 순서대로 가장 밑으로 옮긴다.
2) 옮긴 후 가장 위에 올라와 있는 카드 한 장을 상대에게 넘긴다.
위 1)~2) 행동을 N-1번 수행하고 마지막에는 남은 카드 한 장을 넘긴다.
위 규칙대로 카드를 넘겼을 때, 상대방에게 넘긴 카드 번호를 넘긴 순서대로 출력하시오. 
*/

#include <iostream>
#include <queue>
using namespace std;
 
#define MAXN (100)
int N;
int sol[MAXN + 10];
 
queue <int> que;
void Solve(void){
    int k = 0;
    que = {};
    
    for (int i=1; i<=N; i++){
        que.push(i);
    }
    for (int i=0; i<N-1; i++){
        int cnt = que.back() / 2;
        for (int j=0; j<cnt; j++){
            int r = que.front(); que.pop();
            que.push(r);
        }
        sol[k++] = que.front(); que.pop();
    }
    sol[k++] = que.front(); que.pop();
}
 
void InputData(){
    cin >> N;
}
 
void OutputData(){
    for (int i=0; i<N; i++){
        cout << sol[i] << "\n";
    }
}
 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    InputData();//입력
    Solve();//여기서부터 작성
    OutputData();//출력
    return 0;
}
