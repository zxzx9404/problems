/*
사탕 공장에서는 요구에 따라 다양한 개수의 사탕을 담고 있는 포장을 하고 있다. 어느 날 갑자기 대형 이벤트가 생겨서 공장에 있는 모든 사탕들을 풀어서 하나로 포장 해야 한다.
 
A, B, C 3개의 사탕 포장이 있을 때 이 포장들을 한번에 하나로 합칠 수는 없고, 한번에 2개씩만 합칠 수 있다. 예를 들면 A와 B를 먼저 합친 후 C를 다시 합치거나 A와 C를 먼저 합치고 B를 합치기, 혹은 B와 C를 먼저 합치고 A를 합칠 수 있다.
 
사탕 포장을 풀었다가 다시 합치는 순서는 매우 중요한데, 그 이유는 그 순서에 따라 전체 비용이 달라지기 때문이다.
 
사탕 포장 A와 B에 각각 a개와 b개의 사탕이 들어있다고 할 때 이 둘을 합치는 비용은 a + b라고 한다. 그러므로 A와 B를 먼저 합치고 C를 합치는 경우 그 전체 비용은 a + b + a + b + c이며, B와 C를 먼저 합치고 A를 합치는 비용은 b + c + b + c + a 이므로 그 둘은 서로 같지 않을 수 있다.
 
예를 들어, 각각 2, 2, 5개가 포장되어 있다면 A(2)와 B(2)를 합치는 비용은 4. 합쳐진 것(4)과 C(5)를 합치는 비용은 9로 총 13이 최소비용이다.
 
현재 공장에 포장되어 있는 포장 개수 N과 각각 포장에 들어있는 사탕의 개수 ni가 주어질 때, 이들을 하나로 합치는데 들어가는 비용의 최소(C)를 구하라.
*/

#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

#define MAXN ((int)5e3)
int N;
int A[MAXN + 10];

void InputData(){
	cin >> N;
	for (int i=0; i<N; i++){
		cin >> A[i];
	}
}

int Solve() {
    int temp = 0;
    priority_queue<int, vector<int>, greater<int>> minHeap;

    for (int i=0; i<N; i++) {
        minHeap.push(A[i]);
    }

    for (int i=0; i<N-1; i++) {
        int n1 = minHeap.top();
        minHeap.pop();
        int n2 = minHeap.top();
        minHeap.pop();

        temp += (n1 + n2);

        minHeap.push((n1 + n2));
    }
    
    
    return temp;
}

int main(){
	int ans = -1;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();//입력

	//여기서부터 작성
    ans = Solve();

	cout << ans << "\n";
	return 0;
}




/*
다른 풀이

#include <iostream>
#include <algorithm>
using namespace std;
 
#define MAXN ((int)5e3)
int N;
int A[MAXN + 10];
void simplesort(int s, int e){
    for (int i=s; i<s+2; i++){//2개만 정렬
        for (int j=i+1; j<=e; j++){
            if (A[i] > A[j]){
                swap(A[i], A[j]);
            }
        }
    }
}
 
int Solve(){
    int sum = 0;
    for (int i=0; i<N-1; i++){
        //1.i번째 요소 부터 정렬(정렬 개수는 N-i)
        //sort(A+i, A+N);
        simplesort(i, N-1);
        //2.최솟값 두개 합치기
        A[i+1] += A[i];
        sum += A[i+1];
    }
    return sum;
}
 
void InputData(){
    cin >> N;
    for (int i=0; i<N; i++){
        cin >> A[i];
    }
}
int main(){
    int ans = -1;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    InputData();//입력
 
    ans = Solve();//여기서부터 작성
 
    cout << ans << "\n";
    return 0;
}
*/
