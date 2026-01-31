def binary_search(data, target):
    """
    Binary search for exact match.
    Data must be sorted.

    :param data: sorted list of strings
    :param target: string to search
    :return: index of target or -1
    """
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
