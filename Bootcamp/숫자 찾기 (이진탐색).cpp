/*
오름차순의 순서대로 정렬되어 있는 N개의 데이터에서 특정한 숫자가 몇 번째 위치에 있는지를 알아내는 프로그램을 작성하시오.

첫 번째 줄에 N(1≤N≤50,000)이 주어진다. N은 정렬되어 주어지는 데이터의 수이다.
두 번째 줄에는 N개의 서로 다른 수가 정렬되어 주어진다. 각 수는 공백 하나로 분리되어 주어진다.
세 번째 줄에는 데이터에서 찾아야 할 특정한 수의 개수 T(1≤T≤10,000)가 주어진다. 즉, T가 3이면 3개의 수를 정렬된 데이터에서 찾아야 한다.
네 번째 줄에는 T개의 수가 공백 하나로 분리되어 주어진다.

찾아야 할 수가 정렬되어 주어진 데이터의 수 중에서 앞에서부터 몇 번째에 있는지 그 위치를 출력한다. 첫 번째 위치는 1이다. 만약, 찾으려는 수가 주어지는 데이터에 존재하지 않는다면, 0을 출력한다.

*/

#include <iostream>
#include <unordered_map>
using namespace std;
#define MAXN ((int)5e4)
#define MAXT ((int)1e4)
unordered_map<int, int> A;
int N;
int T;
int B[MAXT+10];

void InputData(){
	cin >> N;
	for(int i=0 ; i<N ; i++){
        int temp;
		cin >> temp;
        A.insert({temp, i+1});
	}
	cin >> T;
	for(int i=0 ; i<T ; i++){
		cin >> B[i];
	}
}
void OutputData(){
	for(int i=0; i<T ; i++){
		cout << B[i] << "\n";
	}
}

void Solve() {
    for (int i=0; i<T; i++) {
        B[i] = A[B[i]];
    }
}


int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();// 입력받는 부분

	// 여기서부터 작성
    Solve();
	OutputData();// 출력하는 부분
	return 0;
}


/*
#include <iostream>
using namespace std;
#define MAXN ((int)5e4)
#define MAXT ((int)1e4)
int N;
int A[MAXN+10];
int T;
int B[MAXT+10];
 
int BinarySearch(int s, int e, int d){
    while (s<=e){
        int m = (s+e)/2;
        if (A[m] == d) {
            return m;
        }
        else if (A[m] > d) {
            e = m-1;
        }
        else{
            s = m+1;
        }
    }
    return 0;
}
 
void Solve(){
    for (int i=0; i<T; i++){
        B[i] = BinarySearch(0, N-1, B[i]);
    }
}
 
void InputData(){
    cin >> N;
    for(int i=1 ; i<=N ; i++){
        cin >> A[i];
    }
    cin >> T;
    for(int i=0 ; i<T ; i++){
        cin >> B[i];
    }
}
void OutputData(){
    for(int i=0; i<T ; i++){
        cout << B[i] << "\n";
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    InputData();// 입력받는 부분
 
    Solve();// 여기서부터 작성
 
    OutputData();// 출력하는 부분
    return 0;
}
*/
