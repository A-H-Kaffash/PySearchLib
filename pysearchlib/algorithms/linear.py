from pysearchlib.core.matcher import wildcard_match


def linear_search(data, pattern):
    """
    Linear search over iterable data using wildcard matching.

    :param data: iterable of strings
    :param pattern: wildcard pattern
    :return: list of matched items
    """
    results = []

    for item in data:
        if wildcard_match(pattern, item):
            results.append(item)

    return results


#tests:
'''
data = [
    "error.log",
    "system.log",
    "readme.txt",
    "file1.txt",
    "file12.txt"
]

a = linear_search(data, "*.log")
# ['error.log', 'system.log']

b = linear_search(data, "file?.txt")
# ['file1.txt']

print(a, b, sep="\n")
'''