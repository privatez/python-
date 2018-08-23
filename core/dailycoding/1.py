"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

"""
solution:
循环数组 拿数组中的两个数字做数学运算然后和目标 k 做比较

evolution: 怎么获取两个目标数字
O(N^2): 双层循环
O(N): 使用数字的值作为 key, 当前下标为 value 存放在字典中
"""

def two_nums_1(nums: [], k: int):
    size = len(nums)
    for i in range(size):
        for j in range(size - i - 1):
            if nums[i] + nums[j + i + 1] == k:
                return True

    return False


def two_nums_2(nums: [], k: int):
    obj = {}

    for i in range(len(nums)):

        if k - nums[i] in obj:
            return True

        obj.setdefault(nums[i], i)

    return False


if __name__ == '__main__':
    k = 17
    nums = [10, 15, 3, 7]
    print(two_nums_1(nums, k))
    print(two_nums_2(nums, k))
