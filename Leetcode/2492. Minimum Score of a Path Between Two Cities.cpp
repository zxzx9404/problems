class Solution {
 public:
  int minScore(int n, vector<vector<int>>& roads) {
    int ans = 10000;
    vector<vector<pair<int, int>>> graph(n);
    queue<int> q{{0}};
    vector<bool> visited(n);
    visited[0] = true;

    for (const vector<int>& r : roads) {
      const int u = r[0] - 1;
      const int v = r[1] - 1;
      const int distance = r[2];
      graph[u].emplace_back(v, distance);
      graph[v].emplace_back(u, distance);
    }

    while (!q.empty()) {
      const int now = q.front();
      q.pop();
      for (const auto& [c, cost] : graph[now]) {
        ans = min(ans, cost);
        if (visited[c])
          continue;
        q.push(c);
        visited[c] = true;
      }
    }

    return ans;
  }
};
