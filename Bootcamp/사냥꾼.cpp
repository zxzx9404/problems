/*
KOI 사냥터에는 N 마리의 동물들이 각각 특정한 위치에 살고 있다. 사냥터에 온 사냥꾼은 일직선상에 위치한 M 개의 사대(총을 쏘는 장소)에서만 사격이 가능하다. 편의상, 일직선을 x-축이라 가정하고, 사대의 위치 x1, x2, ... xM 은 x-좌표 값이라고 하자. 각 동물이 사는 위치는 (a1, b1), (a2, b2), ..., (aN, bN) 과 같이 x, y-좌표 값으로 표시하자. 동물의 위치를 나타내는 모든 좌표 값은 양의 정수이다.
사냥꾼이 가지고 있는 총의 사정거리가 L 이라고 하면, 사냥꾼은 한 사대에서 거리가 L 보다 작거나 같은 위치의 동물들을 잡을 수 있다고 한다. 단, 사대의 위치 xi와 동물의 위치 (aj,bj) 간의 거리는 |xi-aj| + bj 로 계산한다.
예를 들어, 아래의 그림과 같은 사냥터를 생각해보자. (사대는 작은 사각형으로, 동물의 위치는 작은 원으로 표시되어 있다.) 사정거리 L이 4라고하면, 점선으로 표시된 영역은 왼쪽에서 세 번째 사대에서 사냥이 가능한 영역이다.

사대의 위치와 동물들의 위치가 주어졌을 때, 잡을 수 있는 동물의 수를 출력하는 프로그램을 작성하시오.

입력의 첫 줄에는 사대의 수 M(1≤M≤100,000) 동물의 수 N(1≤N≤100,000), 사정거리 L(1≤L≤1,000,000,000)이 빈칸을 사이에 두고 주어진다. 두 번째 줄에는 사대의 위치를 나타내는 M개의 x-좌표 값이 빈칸을 사이에 두고 양의 정수로 주어진다. 이후 N 개의 각 줄에는 각 동물의 사는 위치를 나타내는 좌표 값이 x-좌표 값, y-좌표 값의 순서로 빈칸을 사이에 두고 양의 정수로 주어진다. 사대의 위치가 겹치는 경우는 없으며, 동물들의 위치가 겹치는 경우도 없다. 모든 좌표 값은 1,000,000,000 보다 작거나 같은 양의 정수이다.

input
4 8 4
6 1 4 9 
7 2
3 3
4 5
5 1
2 2
1 4
8 4
9 4

output
6
*/

#include <iostream>
#include <algorithm>
using namespace std;
#define MAXMN ((int)1e5)
int M, N, L;
int X[MAXMN+10];
int A[MAXMN+10];
int B[MAXMN+10];
void InputData(){
	cin >> M >> N >> L;
	for (int i=0; i<M; i++){
		cin >> X[i];
	}
	for (int i=0; i<N; i++){
		cin >> A[i] >> B[i];
	}
}

int BinarySearch(int s, int e, int d) {
    int temp = -1;
    while (s <= e) {
        int m = (s + e) / 2;
        if (X[m] >= d) {
            temp = m;
            e = m - 1;
        }
        else {
            s = m + 1;
        }
    }
    return temp;
}

int Solve() {
    sort(X, X+M);
    int sol = 0;
    
    for (int i=0; i<N; i++) {
        if (B[i] > L) continue;
        int low = A[i] + B[i] - L;
        int up = A[i] + L - B[i];
        int idx = BinarySearch(0, M-1, low);
        if (idx == -1 || X[idx] > up) continue;
        sol++;
    }

    return sol;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int ans = -1;

	InputData();// 입력받는 부분

	//여기서부터 작성
    ans = Solve();
	cout << ans << "\n";// 출력하는 부분
	return 0;
}
