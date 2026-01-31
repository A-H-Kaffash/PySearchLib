from pysearchlib.algorithms.fs_search import file_system_search
from pysearchlib.benchmark.timer import timer
import os

def main():
    search_path = os.getcwd()  # مسیر فعلی پروژه
    pattern = "*.py"

    with timer("File System Wildcard Search"):
        results = file_system_search(search_path, pattern, recursive=True)

    print(f"Searching in: {search_path}")
    print(f"Pattern: {pattern}")
    print(f"Found {len(results)} files")

    for r in results[:10]:  # فقط ۱۰ تای اول
        print(" -", r)

if __name__ == "__main__":
    main()
