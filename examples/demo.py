import os

from pysearchlib.algorithms.linear import linear_search
from pysearchlib.algorithms.binary import binary_search
from pysearchlib.algorithms.prefix import prefix_search
from pysearchlib.algorithms.fs_search import file_system_search
from pysearchlib.utils.dataset import generate_sample_data
from pysearchlib.benchmark.timer import timer


def demo_wildcard_search():
    data = generate_sample_data(10000)
    pattern = "*.log"

    with timer("Linear Wildcard Search"):
        results = linear_search(data, pattern)

    print(f"[Wildcard] Found {len(results)} items")


def demo_binary_search():
    data = sorted(generate_sample_data(10000))
    target = "file100.log"

    with timer("Binary Exact Search"):
        index = binary_search(data, target)

    print(f"[Binary] Target '{target}' found at index: {index}")


def demo_prefix_search():
    data = generate_sample_data(10000)
    prefix = "file1"

    with timer("Prefix Search"):
        results = prefix_search(data, prefix)

    print(f"[Prefix] Found {len(results)} items")


def demo_file_system_search():
    path = os.getcwd()
    pattern = "*.py"

    with timer("File System Search"):
        results = file_system_search(path, pattern, recursive=True)

    print(f"[FS] Found {len(results)} files")


def main():
    print("=== PySearchLib Demo ===\n")

    demo_wildcard_search()
    demo_binary_search()
    demo_prefix_search()
    demo_file_system_search()


if __name__ == "__main__":
    main()
