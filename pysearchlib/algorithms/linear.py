from pysearchlib.core.matcher import wildcard_match
from pysearchlib.utils.normalize import normalize_text


def linear_search(data, pattern, case_insensitive=True):
    results = []

    norm_pattern = normalize_text(pattern, case_insensitive)

    for item in data:
        norm_item = normalize_text(item, case_insensitive)
        if wildcard_match(norm_pattern, norm_item):
            results.append(item)  # خروجی = مقدار اصلی

    return results
