class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""

        counter = defaultdict(int)
        for i in t:
            counter[i] += 1

        left, right = n, m
        ans = deque()

        while left <= right:
            mid = (left + right) // 2

            temp = deque()
            flag = False
            cnt = n
            temp_counter = copy.deepcopy(counter)

            # print("-----new while in-----")
            # print(f"left : {left}, right : {right}, mid : {mid}")

            for i in range(mid):
                temp.append(s[i])
                if counter[s[i]]:
                    if temp_counter[s[i]] > 0:
                        cnt -= 1
                    temp_counter[s[i]] -= 1
                    if not cnt:
                        flag = True
                        ans = temp
            # print("temp counter after first :", temp_counter)
            # aaa = "".join(temp)
            # print(f"cnt : {cnt}, temp : {aaa}")
            if not flag:
                for i in range(mid, m):
                    temp.append(s[i])
                    a = temp.popleft()

                    if counter[a]:
                        temp_counter[a] += 1
                        if temp_counter[a] > 0:
                            cnt += 1

                    if counter[s[i]]:
                        if temp_counter[s[i]] > 0:
                            cnt -= 1
                        temp_counter[s[i]] -= 1
                        if not cnt:
                            flag = True
                            ans = temp
                            break
                    # if mid == 4:
                    #     print(''.join(temp), 'cnt :', cnt)
                    #     print(temp_counter)
                    #     if ''.join(temp) == "cwae":
                    #         print('!!!!')
                    #         print(f'cnt :', cnt)
                    #         print(temp_counter)
                    #         print('!!!!')

            # print("temp counter after for loop :", temp_counter)
            # aaa = "".join(temp)
            # print(f"cnt : {cnt}, temp : {aaa}")

            if flag:
                right = mid - 1
                # print(f"can make {t}")
            else:
                left = mid + 1
                # print(f"cannot make {t}")

        return "".join(ans)
