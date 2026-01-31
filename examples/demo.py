from pysearchlib.algorithms.prefix import prefix_search
from pysearchlib.utils.dataset import generate_sample_data
from pysearchlib.benchmark.timer import timer

def main():
    data = generate_sample_data(10000)
    prefix = "file1"

    with timer("Prefix Search"):
        results = prefix_search(data, prefix)

    print(f"Prefix: {prefix}")
    print(f"Found {len(results)} items")

    for r in results[:10]:
        print(" -", r)

if __name__ == "__main__":
    main()
