/*
다음 명령을 처리하기 위한 큐 함수를 구현하시오.
주어진 명령은 다음의 3가지 이다.
1. "1 a"는 a라는 수를 큐에 넣는다. 이때, a는 10,000 이하의 자연수이다.
2. "0"는 큐에서 데이터를 빼고, 그 데이터를 출력한다. 만약 큐가 비어있으면, "E"를 출력한다.
3. "2"는 큐에 쌓여있는 데이터의 수를 출력한다.
C++의 queue class member functions과 유사한 기능을 하는 아래 함수를 구현하시오
*/

#include <iostream>
using namespace std;

#define MAXN ((int)1e4)
int N;//명령개수
int cmd[MAXN + 10];
int a[MAXN + 10];

int que[MAXN + 10];
int wp, rp;
void push(int d){
    que[wp++] = d;
}
void pop() {
    rp++;
}
int front() {
    return que[rp];
}
bool empty() {
    if (wp == rp) {
        return true;
    }
    return false;
}
int size() {
    return wp - rp;
}
void Solve(){
	wp = rp = 0;//초기화
	for (int i=0; i<N; i++){
		switch(cmd[i]){
		case 0://읽고 제거
			if (empty()) {
				cout << "E" << "\n";
			}
			else{
				cout << front() << "\n";
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
