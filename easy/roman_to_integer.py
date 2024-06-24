#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. 
# However, the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX. 

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.


class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }

        result = 0
        list_s = list(s)
        list_s.reverse()

        for index, value in enumerate(list_s):
            previous = list_s[index - 1]
            if index != 0 and value == "I" and (previous == "V" or previous == "X"):
                result -= dict.get(value)
            elif index != 0 and value == "X" and (previous == "L" or previous == "C"):
                result -= dict.get(value)
            elif index != 0 and value == "C" and (previous == "D" or previous == "M"):
                result -= dict.get(value)
            else:
                result += dict.get(value)

        return result
            
print(Solution().romanToInt("MCMXCIV"))
        
                

        