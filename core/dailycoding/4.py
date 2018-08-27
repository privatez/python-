"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def first_missing_positive(nums: []):
    min_num = 1
    max_num = 1

    new_nums = set()

    for i in nums:
        if i > 0:
            new_nums.add(i)

            if i < min_num:
                min_num = i

            if i > max_num:
                max_num = i

    if min_num != 1:
        return 1

    for i in range(1, max_num + 1):
        if i not in new_nums:
            return i

    return max_num + 1


if __name__ == '__main__':
    print(first_missing_positive([3, 4, -1, 1, 1, 2]))
    print(first_missing_positive([1, 2, 0]))
    print(first_missing_positive([-1, -2, 0]))
    print(first_missing_positive([7, 9]))
