"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""


def solution(nums: []):
    nums_sum = 1
    nums_size = len(nums)
    new_nums = []

    for i in range(nums_size):
        nums_sum *= nums[i]

    for i in range(nums_size):
        new_nums.append(nums_sum // nums[i])

    return new_nums


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5]))
    print(solution([3, 2, 1]))
