class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num2Len = len(num2)
        ans = ""
        for i, n1 in enumerate(num1[::-1]):
            index, flag = num2Len - 1, 0
            t = ""
            while index >= 0:
                d = int(n1) * int(num2[index]) + flag
                r = d % 10
                t = str(r) + t
                flag = d // 10
                index -= 1
            if flag != 0:
                t = str(flag) + t
            t += "0"*i
            if ans == "":
                ans = t
            else:
                tLen, ansLen = len(t), len(ans)
                minLen, maxLen = min(tLen, ansLen), max(tLen, ansLen)
                index = flag = 0
                ta = ""
                while index < minLen:
                    d = int(t[tLen - index -1]) + int(ans[ansLen - index - 1]) + flag
                    r = d % 10
                    ta = str(r) + ta
                    flag = d // 10
                    index += 1
                while index < maxLen:
                    if maxLen == tLen:
                        d = int(t[tLen - index - 1]) + flag
                    else:
                        d = int(ans[ansLen - index - 1]) + flag
                    r = d % 10
                    ta = str(r) + ta
                    flag = d // 10
                    index += 1
                if flag != 0:
                    ta = str(flag) + ta
                ans = ta
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.multiply("98", "9"))