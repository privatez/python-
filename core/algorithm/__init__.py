def array_k_shift(numbs: [], k: int, left: bool = False):
    """
    数组向右移动 k 位
    [1,2,3,4,5] -> k=1 -> [5,1,2,3,4]

    数组向左移动 k 位
    [1,2,3,4,5] -> k=1 -> [2,3,4,5,1]

    :param numbs: 原数组
    :param k: 
    :param left: 向左移动
    :return:
    """
    if not numbs or k < 0 or k > len(numbs):
        return None

    numbs_size = len(numbs)

    if left:
        k = numbs_size - k

    for i in range(int(numbs_size / 2)):
        tmp = numbs[i]
        numbs[i] = numbs[numbs_size - i - 1]
        numbs[numbs_size - i - 1] = tmp

    for i in range(int(k / 2)):
        tmp = numbs[i]
        numbs[i] = numbs[k - i - 1]
        numbs[k - i - 1] = tmp

    for i in range(int((numbs_size - k) / 2)):
        tmp = numbs[i + k]
        numbs[i + k] = numbs[numbs_size - i - 1]
        numbs[numbs_size - i - 1] = tmp

    return numbs


def is_happy(num: int):
    if num < 0:
        return False

    raw_results = []

    while num != 1:
        raw_result = 0
        while num > 0:
            raw_result += (num % 10) * (num % 10)
            num = num // 10

        num = raw_result

        if num in raw_results:
            return False

        raw_results.append(num)
        print(raw_results)

    return


def two_sum(numbs: [], target: int):
    for i in range(len(numbs)):
        for j in range(len(numbs) - i - 1):
            index = j + i + 1
            if numbs[i] + numbs[index] == target:
                return i, index

    return None


def two_sum_2(numbs: [], target: int):
    obj = {}
    for i in range(len(numbs)):
        cur_num = numbs[i]

        if cur_num in obj:
            return obj[cur_num], i

        obj.setdefault(target - cur_num, i)

    return None
