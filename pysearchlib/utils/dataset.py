def generate_sample_data(n=10000):
    """
    Generate a list of sample file names for testing.
    Example patterns: file1.txt, file2.log, image1.png
    """
    data = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            data.append(f"file{i}.txt")
        elif i % 3 == 1:
            data.append(f"file{i}.log")
        else:
            data.append(f"image{i}.png")
    return data
