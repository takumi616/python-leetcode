#Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #1996
        # 199 6   6
        # 19  9   69
        # 1   9   699
        # 0   1   6991
        if x < 0:
            return False

        reversed = 0
        copied_x = x
        while 0 < x:
            reversed = reversed * 10 + (x % 10)
            x //= 10

        return copied_x == reversed
     
print(Solution().isPalindrome(6996))
print(Solution().isPalindrome(69966))
