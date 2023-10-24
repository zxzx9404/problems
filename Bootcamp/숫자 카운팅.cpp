/*
배열에 오름차순으로 N개의 숫자가 저장되어 있다.
M개의 탐색할 숫자가 주어질 때, 각 숫자가 배열에 몇 개씩 저장되어 있는지 출력하는 프로그램을 작성하시오.

첫째 줄에 N 이 입력된다. (1≤N≤200,000)
둘째 줄에 배열에 저장 되어있는 N개의 숫자가 순서대로 공백으로 구분되어 입력된다.
셋째 줄에 M 이 입력된다. (1≤M≤200,000)
넷째 줄에 M개의 탐색할 숫자가 순서대로 공백으로 구분되어 입력된다.
(이 숫자는 정렬 되어있지 않다)

입력 넷째 줄에서 주어진 탐색할 숫자의 배열 내 저장된 개수를 차례대로 출력한다.

input 
10
1 1 1 6 9 11 13 17 19 20 
2
1 9 

output
3 1

*/

#include <iostream>
#include <unordered_map>
using namespace std;
#define MAX ((int)2e5)

int N;
unordered_map<int, int> A;
int M;
int B[MAX+10];

void InputData(){
	cin >> N;
	for(int i=0 ; i<N ; i++) {
        int temp;
		cin >> temp;

        if (A.find(temp) == A.end()) {
            A.insert({temp, 1});
        } else {
            A[temp]++;
        }
	}

	cin >> M;
	for(int i=0 ; i<M ; i++) {
		cin >> B[i];
	}
}

void OutputData(){
	for(int i=0 ; i<M ; i++) {
		cout << A[B[i]] << " ";
	}
	cout << "\n";
}

int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	// 입력받는 부분
	InputData();

	// 여기서부터 작성


	// 출력하는 부분
	OutputData();
	return 0;
}


/*
#include <iostream>
using namespace std;
 
#define MAX ((int)2e5)
 
int N;
int A[MAX+10];
int M;
int B[MAX+10];
 
int BinarySearchLower(int s, int e, int d){
    int sol=-1;
    while (s<=e){
        int m = (s+e)/2;
        if (A[m] == d){
            sol = m;
            e = m-1;
        }
        else if (A[m] > d){
            e = m-1;
        }
        else {
            s = m+1;
        }
    }
    return sol;
}
 
int BinarySearchUpper(int s, int e, int d){
    int sol=-1;
    while (s<=e){
        int m = (s+e)/2;
        if (A[m] == d){
            sol = m;
            s = m+1;
        }
        else if (A[m] > d){
            e = m-1;
        }
        else {
            s = m+1;
        }
    }
    return sol;
}
 
void Solve(){
    for (int i=0; i<M; i++){
        int lower = BinarySearchLower(0, N-1, B[i]);
        if (lower != -1){
            int upper = BinarySearchUpper(0, N-1, B[i]);
            B[i] = upper - lower + 1;
        }
        else{
            B[i] = 0;
        }
    }
}
 
void InputData(){
    cin >> N;
    for(int i=0 ; i<N ; i++) {
        cin >> A[i];
    }
    cin >> M;
    for(int i=0 ; i<M ; i++) {
        cin >> B[i];
    }
}
 
void OutputData(){
    for(int i=0 ; i<M ; i++) {
        cout << B[i] << " ";
    }
    cout << "\n";
}
 
int main(void){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    // 입력받는 부분
    InputData();
 
    // 여기서부터 작성
    Solve();
 
    // 출력하는 부분
    OutputData();
    return 0;
}
*/
