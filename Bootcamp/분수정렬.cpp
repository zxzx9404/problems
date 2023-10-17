/*
0과 1사이의 분수의 분자와 분모의 값이 0 ~ N인 모든 숫자를 작은 수부터 순서대로 배열하는 프로그램을 작성해보자. 예를 들어 N이 5일 경우 다음과 같다.
0/1 1/5 1/4 1/3 2/5 1/2 3/5 2/3 3/4 4/5 1/1
 
실제 조합되는 경우는 다음과 같다.
0/1, 1/1
0/2, 1/2, 2/2
0/3, 1/3, 2/3, 3/3
0/4, 1/4, 2/4, 3/4, 4/4
0/5, 1/5, 2/5, 3/5, 4/5, 5/5
 
이때, 1/2과 2/4처럼 값이 겹치는 경우 분모가 작은 1/2을 선택한다.

input = 5
output:
0/1
1/5
1/4
1/3
2/5
1/2
3/5
2/3
3/4
4/5
1/1

*/

#include <iostream>
#include <map>
 
using namespace std;
 
int N;//정수
 
void InputData(){ 
    cin >> N; 
}
 
int main() {
    InputData();//입력
    map<double, string> m;
     
    //여기서부터 작성
    for (int i=1; i<N+1; i++) {
        for (int j=0; j<i+1; j++) {
            string a = to_string(j) + "/" + to_string(i);
            m.insert({ static_cast<double>(j) / i, a });
        }
    }
 
    for (const auto& pair : m) {
        cout << pair.second << endl;
    }
 
 
    return 0;
}
