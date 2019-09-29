class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        while n > 1:
            tmp = ""
            i, count = 0, 1
            while i < len(s):
                if (i+1) < len(s) and s[i] == s[i+1]:
                    count += 1
                else:
                    tmp += str(count) + s[i]
                    count = 1
                i += 1
            s = tmp
            n -= 1 
        return s

if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(30))