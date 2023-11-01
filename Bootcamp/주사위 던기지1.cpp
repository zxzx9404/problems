/*
주사위를 던진 횟수 N과 출력형식 M을 입력 받아서 M의 값에 따라 각각 아래와 같이 출력하는 프로그램을 작성하시오.
M = 1 : 주사위를 N번 던져서 나올 수 있는 모든 경우
M = 2 : 주사위를 N번 던져서 중복이 되는 경우를 제외하고 나올 수 있는 모든 경우
M = 3 : 주사위를 N번 던져서 모두 다른 수가 나올 수 있는 모든 경우
* 중복의 예
1 1 2 와 중복 : 1 2 1, 2 1 1
1 2 3 과 중복 : 1 3 2, 2 1 3, 2 3 1, 3 1 2
input
3 1

output
1 1 1
1 1 2
1 1 3
1 1 4
1 1 5
1 1 6
1 2 1
…
6 6 6
*/

#include <iostream>
#include <vector>
using namespace std;

int N, M;

void M1(int c, vector<int> arr) {
    if (c == N) {
        for (int i = 0; i < arr.size(); i++) {
            cout << arr[i]<< " ";
        }
        cout << endl;
        return;
    }

    for (int i = 1; i <= 6; i++) {
        arr.push_back(i);
        M1(c + 1, arr);
        arr.pop_back();
    }
}

void M2(int c, vector<int> arr, int ex) {
    if (c == N) {
        for (int i = 0; i < arr.size(); i++) {
            cout << arr[i]<< " ";
        }
        cout << endl;
        return;
    }

    for (int i = ex; i <= 6; i++) {
        arr.push_back(i);
        M2(c + 1, arr, i);
        arr.pop_back();
    }
}

void M3(int c, vector<int> arr, vector<int>& usingArr) {
    if (c == N) {
        for (int i = 0; i < arr.size(); i++) {
            cout << arr[i]<< " ";
        }
        cout << endl;
        return;
    }

    for (int i = 1; i <= 6; i++) {
        if (!usingArr[i]) {
            usingArr[i]= 1;
            arr.push_back(i);
            M3(c + 1, arr, usingArr);
            arr.pop_back();
            usingArr[i]= 0;
        }
    }
}


int main() {
    cin >> N >> M;

    if (M == 1) {
        vector<int> arr;
        M1(0, arr);
    }
    else if (M == 2) {
        vector<int> arr;
        M2(0, arr, 1);
    }
    else if (M == 3) {
        vector<int> arr;
        M3(0, arr);
    }

    return 0;
}
