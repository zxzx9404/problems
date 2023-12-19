#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
struct DATA {
    int s, e;
};
struct Compare {
    bool operator()(const DATA& a, const DATA& b) {
        return a.s > b.s;
    }
};

bool compare(const DATA& a, const DATA& b) {
    return a.e < b.e;
}

int main(){
    int N, a, b, D, ans = 0;
    vector<DATA> temp;
    vector<DATA> roads;
    priority_queue<DATA, vector<DATA>, Compare> pq;
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> a >> b;
        if (a > b) temp.push_back({b, a});
        else temp.push_back({a, b});
    }
    cin >> D;

    for (DATA it: temp) {
        if (it.e - it.s <= D) roads.push_back({it});
    }
    sort(roads.begin(), roads.end(), compare);

    for (DATA it: roads) {
        if (pq.empty()) pq.push(it);
        else {
            while (!pq.empty() && pq.top().s < it.e - D) pq.pop();
            pq.push(it);
        }
        ans = max(ans, static_cast<int>(pq.size()));
    }

    cout << ans << endl;// 출력하는 부분
    return 0;
}
