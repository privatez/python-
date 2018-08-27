def solution(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    print('matrix: {}'.format(matrix))
    new_list = []

    if not matrix or len(matrix) == 0:
        return new_list

    turns = 0
    direction = 0
    m = len(matrix)
    n = len(matrix[0])

    matrix_size = n * m
    while len(new_list) != matrix_size:
        direction += 1

        if direction == 1:
            new_list.append(matrix[turns][turns])
            current_count = n - turns - 1
            for i in range(current_count):
                new_list.append(matrix[turns][i + turns + 1])
        elif direction == 2:
            current_count = m - turns - 1
            for i in range(current_count):
                new_list.append(matrix[i + turns + 1][n - turns - 1])
        elif direction == 3:
            current_count = n - turns - 1
            for i in range(current_count):
                new_list.append(matrix[m - turns - 1][n - i - 2])
        elif direction == 4:
            current_count = m - turns - 2
            for i in range(current_count):
                new_list.append(matrix[m - i - 2][turns])

            turns += 1
            direction = 0

            n = n - turns
            m = m - turns

    return new_list


if __name__ == '__main__':

    def gen_matrix(m, n):
        matrix = []
        num = 0
        for i in range(m):
            raw = []
            for j in range(n):
                num += 1
                raw.append(num)
            matrix.append(raw)
        return matrix


    """
        data = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        # [1,2,3,4,8,12,11,10,9,5,6,7]
    """
    print(solution(gen_matrix(3, 4)))

    """
    [
        [1, 2, 3, 4, 5], 
        [6, 7, 8, 9, 10], 
        [11, 12, 13, 14, 15], 
        [16, 17, 18, 19, 20], 
        [21, 22, 23, 24, 25]
    ]
    """

    print(solution(gen_matrix(5, 5)))
