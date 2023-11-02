/*
해마다 열리는 꿀꿀이 올림피아드에는 여러 종목들이 있는데, 요즘에는 꿀꿀이들의 교양을 겨루는 ‘미술관람 대회’가 인기를 끌고 있다. 
이 대회는 사회자가 빨강, 초록, 파랑으로 이루어진 N × N 픽셀의 그림을 보여주면 그 그림에 포함된 영역의 수를 빠르고 정확하게 맞추는 것이 목표이다. 
동일한 색깔이 네 방향(상, 하, 좌, 우) 중 한 곳이라도 연결되어 있으면 하나의 영역으로 간주한다.
 
예를 들어, 아래 그림은 각각 2, 1, 1개의 빨간색, 초록색, 파란색 영역이 있어 총 4개의 영역이 있다.

한편, 꿀꿀이들의 절반 정도는 선천적인 유전자 때문에 적록색맹이라서 빨간색과 초록색을 구별하지 못한다. 
따라서 사회자는 일반 대회와 적록색맹용 대회를 따로 만들어서 대회를 진행하려고 한다. 사회자를 도와 영역의 수를 구하는 프로그램을 작성하여라.

input
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

output
4 3
*/


#include <iostream>
#include <vector>
using namespace std;

int N;
vector<vector<char>> arr;
vector<vector<int>> visited;
int ans_RGB = 0;
int ans_RG_B = 0;
vector<int> di = {0, 0, -1, 1};
vector<int> dj = {1, -1, 0, 0};

void check_RGB(int st_i, int st_j) {
    vector<pair<int, int>> RGB;
    RGB.push_back(make_pair(st_i, st_j));

    while (!RGB.empty()) {
        int i = RGB.back().first;
        int j = RGB.back().second;
        RGB.pop_back();

        for (int k = 0; k < 4; k++) {
            int ni = i + di[k];
            int nj = j + dj[k];

            if (0 <= ni && ni < N && 0 <= nj && nj < N && !visited[ni][nj]&& arr[i][j]== arr[ni][nj]) {
                visited[ni][nj]= 1;
                RGB.push_back(make_pair(ni, nj));
            }
        }
    }
}

int main() {
    cin >> N;
    arr.resize(N, vector<char>(N));
    visited.resize(N, vector<int>(N, 0));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> arr[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (!visited[i][j]) {
                check_RGB(i, j);
                ans_RGB++;
            }
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (arr[i][j]== 'G') {
                arr[i][j]= 'R';
            }
        }
    }

    visited.assign(N, vector<int>(N, 0));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (!visited[i][j]) {
                check_RGB(i, j);
                ans_RG_B++;
            }
        }
    }

    cout << ans_RGB << " " << ans_RG_B << endl;

    return 0;
}
