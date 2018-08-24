"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II.
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""


def solution(s: str):
    nums = symbol2value(s)
    nums_sum = 0
    index = 0
    while index < len(nums):
        current_value = nums[index]
        next_value = 0

        if index != len(nums) - 1:
            next_value = nums[index + 1]

        if current_value * 5 == next_value or current_value * 10 == next_value:
            nums_sum += next_value - current_value
            index += 1
        else:
            nums_sum += current_value

        index += 1

    return nums_sum


def symbol2value(s: str):
    nums = []
    for i in s:
        if i == "I":
            nums.append(1)
        elif i == "V":
            nums.append(5)
        elif i == "X":
            nums.append(10)
        elif i == "L":
            nums.append(50)
        elif i == "C":
            nums.append(100)
        elif i == "D":
            nums.append(500)
        elif i == "M":
            nums.append(1000)
    return nums


import unittest


class Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution("III"), 3)
        self.assertEqual(solution("IV"), 4)
        self.assertEqual(solution("IX"), 9)
        self.assertEqual(solution("LVIII"), 58)
        self.assertEqual(solution("MCMXCIV"), 1994)


if __name__ == '__main__':
    unittest.main()
