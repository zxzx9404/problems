class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        flag = False

        for i in range(len(str(low)), len(str(high))+1):
            for j in range(1, 10-i+1):
                t = ''
                for k in range(i):
                    t += str(j+k)
                if int(t) <= high:
                    if int(t) < low: continue
                    ans.append(int(t))
                else:
                    flag = True
                    break
                if flag: break
            if flag: break
        return ans
