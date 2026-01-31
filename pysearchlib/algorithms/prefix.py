def prefix_search(data, prefix):
    """
    Prefix-based search (starts with).

    :param data: iterable of strings
    :param prefix: prefix string
    :return: list of matched items
    """
    results = []

    for item in data:
        if item.startswith(prefix):
            results.append(item)

    return results
