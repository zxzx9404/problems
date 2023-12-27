#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <unordered_map>
using namespace std;
int N, M;
unordered_map<int, vector<pair<int, int>>> nodes;
vector<int> visited;
vector<int> FROM;
unordered_map<int, unordered_map<int, bool>> isUsed;

void dijk(int st) {
    visited[st] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    int cost, now, next, c, new_cost;
    pq.push({0, st});

    while (!pq.empty()) {
        cost = pq.top().first;
        now = pq.top().second;
        pq.pop();

        if (visited[now] < cost) continue;

        for (auto& p: nodes[now]) {
            next = p.first;
            c = p.second;
            new_cost = cost + c;
            if (visited[next] > new_cost) {
                visited[next] = new_cost;
                FROM[next] = now;
                pq.push({new_cost, next});
            }
        }
    }
}

int main() {
    int a, b, s;
    cin >> N >> M;
    for (int i=0; i<M; i++) {
        cin >> a >> b >> s;
        nodes[a].push_back({b, s});
        nodes[b].push_back({a, s});
    }
    for (int i=0; i<=N; i++) {   
        visited.push_back(numeric_limits<int>::max());
        FROM.push_back(0);
    }
    

    dijk(1);
    int k, sol = 0;
    vector<pair<int, int>> sol_list;
    for (int i=N; i>0; i--) {
        k = i;
        while (FROM[k] != 0) {
            if (!isUsed[k][FROM[k]]) {
                isUsed[k][FROM[k]] = true;
                sol++;
                sol_list.push_back({k, FROM[k]});
            }
            k = FROM[k];
        }
    }

    cout << sol << '\n';
    for (auto it: sol_list) {
        cout << it.first << ' ' << it.second << '\n';
    }

    return 0;
}
