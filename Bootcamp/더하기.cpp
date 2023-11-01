/*
덧셈을 못하는 철수를 공부시키기 위해 자연수들을 주고, 그 중에 몇 개의 수를 골라서 그 합이 K가 될 수 있는지 알아보라고 시켰다. 
철수 어머니가 자연수들을 무작위로 선택해서 본인도 가능한지 아닌지 모르고 있다. 어머니가 채점을 할 수 있게 주어진 문제의 답을 찾아주자.

첫 번째 줄에 테스트 케이스 개수 T(1≤T≤10)가 주어진다.
두 번째 줄부터 아래 내용이 T개 만큼 주어진다.
첫 줄에 자연수 개수 N(5 <= N <= 20)과 K(1 <= K <= 2,000,000)가 공백으로 구분되어 입력된다.
다음 줄에 N개의 자연수 di(1 <= di <= 100,000)가 공백으로 구분되어 입력된다.

T줄에 걸쳐 각 테스트 케이스 별로 주어진 자연수 중 몇 개의 합이 K가 되면 “YES”를 아니면 “NO”를 출력한다.
*/


#include <iostream>
#include <stack>
using namespace std;
#define MAXN (20)
int N, K;//자연수 개수, 만들수
int A[MAXN+10];//자연수 값
int prefixSum[MAXN+10];
string msg[] = {"NO", "YES"};
struct T {
	int cnt, res;
};

void InputData(){
	cin >> N >> K;
	for (int i=0; i<N; i++){
		cin >> A[i];
	}
}

int Solve() {
	prefixSum[0] = A[0];
	for (int i=1; i<N; i++) {
		prefixSum[i] = prefixSum[i-1] + A[i];
	}
	stack<T> stk;
	stk.push({0, 0});
	// NO = 0, YES = 1
	while (!stk.empty()) {
		T t = stk.top();
		stk.pop();

		if (t.res == K) return 1;
		if (t.res > K) continue;
		if (t.cnt == N) continue;
		if (prefixSum[N-1] - prefixSum[t.cnt-1] + t.res < K) continue;
		stk.push({t.cnt+1, t.res});
		stk.push({t.cnt+1, t.res + A[t.cnt]});
	}
	return 0;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int T, ans = -1;
	cin >> T;
	for(int t=1; t<=T; t++){
		InputData();//입력

		//여기서부터 작성
		ans = Solve();
		cout << msg[ans] << "\n";//출력
	}
	return 0;
}
