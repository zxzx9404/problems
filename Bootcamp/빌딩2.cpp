/*
N개의 빌딩이 있다. 
빌딩은 1번부터 N번까지 번호가 붙어 있다.
빌딩은 X좌표 상에 위치해 있으며 i번 빌딩은 i좌표 상에 위치해 있다. 그리고 각 빌딩은 Hi 만큼의 높이를 가지고 있다.
i < j 이고 Hi < Hj 일 경우, i번 빌딩에서 j번 빌딩을 볼 수 있다. 
각 빌딩에서 현재 빌딩의 좌표보다 뒤에 있는 빌딩을 보고자 할 때, 가장 가까이 보이는 빌딩이 어딘지 찾는 프로그램을 작성하라. 
*/

#include <iostream>
#include <stack>
using namespace std;
#define MAXN ((int)1e5)
int N;//빌딩수
int H[MAXN+10];//빌딩높이
int sol[MAXN+10];//각 빌딩에서 보이는 빌딩 번호

stack <int> stk;

void InputData() {
	cin >> N;
	for (int i=1; i<=N; i++){
		cin >> H[i];
	}
}
 
void Solve(){
    stk = {};
    for (int i=1; i<=N; i++){
        while(!stk.empty() && (H[stk.top()] < H[i])){
            sol[stk.top()] = i;
            stk.pop();
        }
        stk.push(i);
    }
}

void OutputData() {
	for (int i=1; i<=N; i++){
		cout << sol[i] << "\n";
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	InputData();//입력받는 부분

	//여기서부터 작성
    Solve();
	OutputData();//출력하는 부분
	return 0;
}
