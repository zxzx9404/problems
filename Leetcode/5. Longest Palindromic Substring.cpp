class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
        int start = 0, maxLen = 1;

        for (int i = 0; i < n; i++) {
            int len1 = expandAroundCenter(s, i, i);  // 홀수 길이 회문
            int len2 = expandAroundCenter(s, i, i + 1);  // 짝수 길이 회문
            int len = max(len1, len2);

            if (len > maxLen) {
                start = i - (len - 1) / 2;
                maxLen = len;
            }
        }

        return s.substr(start, maxLen);
    }

private:
    int expandAroundCenter(string s, int left, int right) {
        int n = s.length();

        while (left >= 0 && right < n && s[left]== s[right]) {
            left--;
            right++;
        }

        return right - left - 1;
    }
};
