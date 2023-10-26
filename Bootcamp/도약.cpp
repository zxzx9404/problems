/*
개구리가 연못 위에서 놀고 있다. 개구리는 N개의 연 잎 들을 이용해서 이리저리 뛰어 놀고 있다.
 
개구리가 뛰는 장면을 보던 철수는 개구리가 도약을 하는 경우가 얼마나 있는지 궁금해졌다. 여기서 도약은 아래 조건을 만족하는 경우를 말한다.
 
1. 개구리가 뛴 거리가 이전에 뛴 거리 이상 뛰지만 그 2배보다 멀리 뛰지는 않는다.
2. 개구리는 오른쪽으로만 뛴다.
3. 개구리는 두 번만 뛴다.
4. 위 세 가지 조건을 만족한다면 어느 곳에서든 시작할 수 있다.
 
허나, 연 잎 들이 너무 많기 때문에 가능한 횟수가 매우 많아질 것 같다고 생각한 철수는, 개구리가 오른쪽으로 도약하는 경우가 얼마나 되는지 구해달라고 했다. 철수를 위해 프로그램을 짜주자.

첫 번째 줄에는 연 잎의 수 N(3 ≤ N ≤ 1,000)이 주어진다.
두 번째 줄부터 N개의 줄에는 각 연 잎의 좌표가 주어진다. 모든 좌표는 0 이상 108 이하이다.

input
5
3
1
10
7
4

output
4

TC 해설
개구리가 오른쪽으로 도약하는 경우는 다음 4가지뿐이다.
(1, 3, 7), (1, 4, 7), (4, 7, 10), (1, 4, 10)
*/

#include <iostream>
#include <algorithm>
using namespace std;
#define MAXN ((int)1e3)
int N;//연잎수
int A[MAXN+10];//연잎좌표
void InputData(){
	cin >> N;
	for (int i=0; i<N; i++){
		cin >> A[i];
	}
}

int Solve() {
	sort(A, A+N);
	int cnt = 0;

	for (int i=0; i<N-2; i++) {
		for (int j=i+1; j<N-1; j++) {
			int gap1 = A[j] - A[i];
			for (int k=j+1; k<N; k++) {
				int gap2 = A[k] - A[j];
				if (gap2 > gap1 * 2) {
					break;
				}
				if (gap2 >= gap1) {
					cnt++;
				} 
			}
		}
	}

	return cnt;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int ans = -1;
	InputData();//입력받는 부분

	//여기서부터 작성
	ans = Solve();
	cout << ans << "\n";//출력하는 부분
	return 0;
}



/*
#include <iostream>
#include <algorithm>
using namespace std;
#define MAXN ((int)1e3)
int N;//연잎수
int A[MAXN+10];//연잎좌표
int BsLow(int s, int e, int d){//d값 보다 크거나 같은 값 중에 작은 인덱스
    int sol = -1;
    while(s<=e){
        int m=(s+e)/2;
        if (A[m] >= d){
            sol = m;
            e=m-1;
        }
        else{
            s=m+1;
        }
    }
    return sol;
}
int BsUp(int s, int e, int d){//d값 보다 작거나 같은 값 중에 큰 인덱스
    int sol = -1;
    while(s<=e){
        int m=(s+e)/2;
        if (A[m] <= d){
            sol=m;
            s=m+1;
        }
        else{
            e=m-1;
        }
    }
    return sol;
}
int Solve(){
    int cnt = 0;
    sort(A, A+N);
    for (int a=0; a<N-2; a++){//첫번째 연 잎 인덱스
        for (int b=a+1; b<N-1; b++){//두번째 연 잎 인덱스
            int first = A[b] - A[a];//첫번째 뛴 거리
            int low = BsLow(0, N-1, A[b]+first);//크거나 같은 값 중에 작은 인덱스
            if (low < 0) break;
            cnt += BsUp(0, N-1, A[b]+2*first) - low + 1;//작거나 같은 값 중에 큰 인덱스
        }
    }
    return cnt;
}
void InputData(){
    cin >> N;
    for (int i=0; i<N; i++){
        cin >> A[i];
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int ans = -1;
    InputData();//입력받는 부분
  
    ans = Solve();//여기서부터 작성
  
    cout << ans << "\n";//출력하는 부분
    return 0;
}
*/
