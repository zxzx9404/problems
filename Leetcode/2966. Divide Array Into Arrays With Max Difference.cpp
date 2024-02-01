class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        vector<vector<int>> ans;
        int N = nums.size();
        sort(nums.begin(), nums.end());

        for (int i=0; i<N; i+=3) {
            if (nums[i+2] - nums[i] > k) return {};
            ans.push_back({nums[i], nums[i+1], nums[i+2]});

        }

        return ans;

    }
};
