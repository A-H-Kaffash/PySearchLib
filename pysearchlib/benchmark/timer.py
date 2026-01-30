import time
from contextlib import contextmanager

@contextmanager
def timer(name="Operation"):
    start = time.time()
    yield
    end = time.time()
    print(f"{name} took {end - start:.6f} seconds")
