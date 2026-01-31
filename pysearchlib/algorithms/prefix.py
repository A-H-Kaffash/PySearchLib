from pysearchlib.utils.normalize import normalize_text


def prefix_search(data, prefix, case_insensitive=True):
    results = []

    norm_prefix = normalize_text(prefix, case_insensitive)

    for item in data:
        norm_item = normalize_text(item, case_insensitive)
        if norm_item.startswith(norm_prefix):
            results.append(item)

    return results
