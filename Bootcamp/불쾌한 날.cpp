/*
농부 희찬이의 N(1≤N≤80,000)마리의 소들은 "bad hair day"를 맞이하였다. 각 소들이 자신들의 촌스런 머리 모양을 부끄러워 하자, 희찬이는 소들이 다른 소들의 머리 모양을 얼마나 알 수 있는지를 알고자 했다.
i번째 소들은 키가 hi(1≤hi≤1,000,000,000) 이며, 동쪽(오른쪽)을 바라보고 서있다. 따라서, i번째 소는 자신의 앞 ( i+1, i+2,...)의 소들의 머리 모양만 볼 수 있으며, 앞에 자신의 키와 같거나 큰 소가 서 있을 경우 그 소의 앞에 있는 소들의 머리 모양을 볼 수 없다.

1(5) - 2(2) - 3(4) - 4(2) - 5(6) - 6(1)

다음 예제를 고려해보자: ()의 숫자는 키를 나타낸다.
1번 소는 2,3,4번소의 머리 모양을 볼 수 있다.
2번 소는 어떤 소의 머리 모양도 볼 수 없다.
3번 소는 4번 소의 머리 모양을 볼 수 있다.
4번 소는 어떤 소의 머리 모양도 볼 수 없다. 
5번 소는 6번 소의 머리 모양을 볼 수 있다.
6번 소는 모든 소들의 머리 모양을 볼 수 없다!
i번 소들이 볼 수 있는 머리 모양의 수를 Ci 이라고 할 때, C1부터 CN 까지의 합을 출력하는 프로그램을 작성하라. 위의 예제의 답은 3+0+1+0+1+0=5가 된다.

*/

#include <iostream>
#include <stack>
using namespace std;
 
#define MAXN ((int)8e4)
int N;
int H[MAXN + 10];
 
stack <int> stk;
 
long long Solve(){
    long long cnt = 0;
 
    stk = {};
 
    for (int i=0; i<N; i++){
        while(!stk.empty() && (stk.top() <= H[i])) {
            stk.pop();
        }
        cnt += stk.size();
        stk.push(H[i]);
    }
    return cnt;
}
 
void InputData(){
    cin >> N;
    for (int i=0; i<N; i++){
        cin >> H[i];
    }
}
 
int main(){
    long long ans = -1;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    InputData();//입력
 
    ans = Solve();//여기서부터 작성
 
    cout << ans << "\n";//출력
    return 0;
}
