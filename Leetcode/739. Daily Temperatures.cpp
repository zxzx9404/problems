class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int N = temperatures.size();
        vector<int> ans(N, 0);
        stack<int> stk;

        for (int i=0; i<N; i++) {
            while (!stk.empty() && temperatures[stk.top()] < temperatures[i]) {
                ans[stk.top()] = i - stk.top();
                stk.pop();
            }
            stk.push(i);
        }

        return ans;
    }
};
