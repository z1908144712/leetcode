class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = float(1.0)
        flag = False
        if n == 0:
            return 1
        elif n < 0:
            flag = True
            n = -n
        count = 0
        f = float(1.0)
        while n > 0:
            f *= x
            count += 1
            if count > n:
                count = 0
                f = 1.0
                continue
            ans *= f
            n -= count
        if flag:
            return 1 / ans
        else:
            return ans

if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2.1000, 3))