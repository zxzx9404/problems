// N개의 자연수가 주어질 때 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

#include <iostream>
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

void OutputData(){
    for (int i=0; i<N; i++){
        cout << A[i] << " ";
    }
    cout << "\n";
}

void Solve() {
    for (int i=0; i<N-1; i++) {
        for (int j=0; j<N-i-1; j++) {
            if (A[j] < A[j+1]) {
                int temp = A[j];
                A[j] = A[j+1];
                A[j+1] = temp;
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    InputData();//입력 받는 부분
    
    //여기서부터 작성
    Solve();
    OutputData();//출력 하는 부분
    return 0;
}
