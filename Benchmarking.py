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

def graph_times(results, size):
    ks = results.keys()
    times = results.values()
    plt.scatter(ks, times)
    plt.xlabel("k value")
    plt.ylabel("times (seconds)")
    plt.title("Size: " + str(size))
    savefig = str(len(ks)) + "k_results" + str(size) + ".png"
    plt.savefig(savefig)
    plt.close()

def benchmark_loop(size_range):
    number = 1 #number of arrays to make of each size
    for size in size_range:
        results = {}
        for k in [1, len(size)//2, len(size) - 1]:
            results.setdefault(k, benchmark(size, number, k))
        graph_times(results, size)
def main():

    sizes = [10_000_000
             ,50_000_000
             ,100_000_000
             ,200_000_000
             ,500_000_000
             ]
    sizes = [1_000_000
             ,5_000_000
             ,10_000_000
             ,50_000_000
             ,100_000_000
             ]
    benchmark_loop(sizes)

if __name__ == "__main__":
    main()