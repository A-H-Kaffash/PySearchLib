import os
from pysearchlib.core.matcher import wildcard_match


def file_system_search(root_path, pattern, recursive=True):
    """
    Search files in filesystem using wildcard pattern.

    :param root_path: directory to search
    :param pattern: wildcard pattern (e.g. *.log)
    :param recursive: search in subdirectories or not
    :return: list of matched file paths
    """
    results = []

    if recursive:
        for root, _, files in os.walk(root_path):
            for file in files:
                if wildcard_match(pattern, file):
                    results.append(os.path.join(root, file))
    else:
        for file in os.listdir(root_path):
            full_path = os.path.join(root_path, file)
            if os.path.isfile(full_path):
                if wildcard_match(pattern, file):
                    results.append(full_path)

    return results
