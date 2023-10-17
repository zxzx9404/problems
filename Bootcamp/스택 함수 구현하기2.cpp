/*
다음 명령을 처리하기 위한 스택 함수를 구현하시오.

주어진 명령은 다음의 3가지이다.
1. "1 a"는 a라는 수를 스택에 넣는다. 이때, a는 10,000 이하의 자연수이다.
2. "0"는 스택에서 데이터를 빼고, 그 데이터를 출력한다. 만약 스택이 비어있으면, "E"를 출력한다.
3. "2"는 스택에 쌓여있는 데이터의 수를 출력한다.

C++의 stack class member functions과 유사한 기능을 하는 아래 함수를 구현하시오
*/

#include <iostream>
using namespace std;

#define MAXN ((int)1e4)
int N;//명령개수
int cmd[MAXN + 10];
int a[MAXN + 10];

int stk[MAXN + 10];
int sp;
void push(int d){
    stk[sp++] = d;
}
void pop() {
    sp--;
}
int top() {
    return stk[sp-1];
}
bool empty() {
    if (sp == 0) {
        return true;
    }
    return false;
}
int size() {
    return sp;
}
void Solve(){
	sp = 0;//초기화
	for (int i=0; i<N; i++){
		switch(cmd[i]){
		case 0://읽고 제거
			if (empty()) {
				cout << "E" << "\n";
			}
			else{
				cout << top() << "\n";
				pop();
			}
			break;
		case 1://저장
			push(a[i]);
			break;
		default://2 : 저장 개수
			cout << size() << "\n";
		}
	}
}
void InputData(){
	cin >> N;
	for (int i=0; i<N; i++){
		cin >> cmd[i];
		if (cmd[i] == 1){
			cin >> a[i];
		}
	}
}
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();
	Solve();
	return 0;
}
