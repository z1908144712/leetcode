class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # def match(s, p):
        #     #print(s, p)
        #     if len(p) == 0:
        #         return len(s) == 0
        #     else:
        #         if len(s) > 0:
        #             if s[0] == p[0] or p[0] == "?":
        #                 return match(s[1:], p[1:])
        #             elif p[0] == "*":
        #                 return match(s, p[1:]) or match(s[1:], p)
        #             else:
        #                 return False
        #         else:
        #             return p[0] == "*" and match(s, p[1:])
        # i = 0
        # while i < len(p) - 1:
        #     if p[i] == "*" and p[i+1] == "*":
        #         p = p[:i+1] + p[i+2:]
        #     else:
        #         i += 1
        # return match(s, p)
        slen, plen = len(s), len(p)
        f = [[False] * (plen+1) for i in range(slen+1)]
        f[0][0] = True
        i = 1
        while i <= plen:
            f[0][i] = f[0][i-1] and (p[i-1] == "*")
            i += 1
        i = 1
        while i <= slen:
            j = 1
            while j <= plen:
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    f[i][j] = f[i-1][j-1]
                if p[j-1] == "*":
                    f[i][j] = f[i][j-1] or f[i-1][j]
                j += 1
            i += 1
        return f[slen][plen]
if __name__ == "__main__":
    sol = Solution()
    s = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
    p = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"
    print(sol.isMatch(s, p))