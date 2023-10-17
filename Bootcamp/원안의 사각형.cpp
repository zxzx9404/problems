/*
원의 반지름(R) 이 주어졌을 때, 원 안에 1*1짜리 정사각형이 몇 개가 있을 수 있는지 구하는 프로그램을 작성하시오.
예를 들어, 반지름 2가 주어지면 아래와 같이 배치된다.
그러면 원안에는 4개의 정사각형이 있을 수 있다.

input 2 -> output 4
input 4 -> output 32
input 5 -> output 60
input 7 -> output 120
*/

#include <iostream>
#include <cmath>
using namespace std;

int R;//원의 반지름

void InputData(){
	cin >> R;
}

int main() {
	int ans = 0;
	InputData();//입력
	
	//여기서부터 작성
	for (int i = 1; i < R; i++) {
	    for (int j = 1; j < R; j++) {
	        if (pow(i, 2) + pow(j, 2) <= pow(R, 2)) {
	            ans++;
	        }
	    }
	}
	
	cout << ans * 4 << endl;//출력
	return 0;
}
