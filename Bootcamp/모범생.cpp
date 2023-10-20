/*
N명의 점수가 주어질 때 상위 3명의 ID를 출력하는 프로그램을 작성하시오.
i 번째 유저의 아이디는 i
점수가 같다면 id가 작은 순으로 출력
*/

#include <iostream>
#include <vector>
using namespace std;
#define MAXN ((int)3e4)
int N;
pair<int, int> A[MAXN + 10];

void InputData(){
	cin >> N;
	for (int i=0; i<N; i++){
        int n;
        cin >> n;
        A[i] = make_pair(n, i+1);
	}
}

void OutputData(){
	for (int i=0; i<3; i++){
		cout << A[i].second << " ";
	}
	cout << "\n";
}

void QuickSort(int start, int end){
    if(start >= end){
        // 원소가 1개인 경우
        return; 
    }
    
    int pivot = start;
    int i = pivot + 1; // 왼쪽 출발 지점 
    int j = end; // 오른쪽 출발 지점
    pair<int, int> temp;
    
    while(i <= j){
        // 포인터가 엇갈릴때까지 반복
        while(i <= end && (A[i].first > A[pivot].first || (A[i].first == A[pivot].first && A[i].second < A[pivot].second))){
            i++;
        }
        while(j > start && (A[j].first < A[pivot].first || (A[j].first == A[pivot].first && A[j].second > A[pivot].second))){
            j--;
        }
        
        if(i > j){
            // 엇갈림
            temp = A[j];
            A[j] = A[pivot];
            A[pivot] = temp;
        }else{
            // i번째와 j번째를 스왑
            temp = A[i];
            A[i] = A[j];
            A[j] = temp;
        }
    } 
    
    // 분할 계산
    QuickSort(start, j - 1);
    QuickSort(j + 1, end);
}
 

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();//입력 받는 부분

	//여기서부터 작성
    QuickSort(0, N-1);

	OutputData();//출력 하는 부분
	return 0;
}
