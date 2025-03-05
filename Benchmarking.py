import random
import time
import matplotlib.pyplot as plt

import Selection

def get_arrays(size, number):
    rand = random.Random()
    arrays = []
    for i in range(number):
        arr = []
        for j in range(size):
            arr.append(rand.random() * 1000)
        arrays.append(arr)
    return arrays

def select(A, k):
    return Selection.selection(A, k)

def benchmark(size, number, k):
    arrays = get_arrays(size, number)
    times = []
    for i in range(number):
        start_time = time.time()
        select(arrays[i], k)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def graph_times(results):
    sizes = results.keys()
    times = results.values()
    plt.scatter(sizes, times)
    plt.xlabel("sizes")
    plt.ylabel("times (seconds)")
    plt.show()

def main():
    results = {}
    size = 1_000_000
    ks = []
    for k in range(1, 1_000_000, 500):
        ks.append(k)
    number = 1
    for k in ks:
        results.setdefault(size, benchmark(size, number, k))
    graph_times(results)



if __name__ == "__main__":
    main()