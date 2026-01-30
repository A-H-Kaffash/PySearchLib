from pysearchlib.algorithms.linear import linear_search
from pysearchlib.benchmark.timer import timer
from pysearchlib.utils.dataset import generate_sample_data

def main():
    data = generate_sample_data(10000)  # 10k فایل
    pattern = "*.log"

    with timer("Linear Wildcard Search on 10k items"):
        results = linear_search(data, pattern)

    print(f"Pattern: {pattern}")
    print(f"Found {len(results)} items")

if __name__ == "__main__":
    main()
