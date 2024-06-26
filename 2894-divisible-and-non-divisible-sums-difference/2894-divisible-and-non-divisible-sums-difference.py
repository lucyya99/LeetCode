class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # num1 : [1, n] 중에 m으로 안나눠지는거의 합
        # num2 : [1, n] 중에 m으로 나눠지는거의 합
        # num1 - num2
        result = 0
        for i in range(1, n+1):
            if i % m == 0:
                result -= i
            else:
                result += i
        return result