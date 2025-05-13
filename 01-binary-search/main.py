import search
import time

def main():
    # 1. Simple Search

    # Simple search, a searching algorithm that runs O(n) (linear time), is a searching alg-
    # orithm that checks each particular value in an array or list one-by-one from begining
    # until the end of the array or list.
    nums = list(range(1024))
    target = -1

    start = time.perf_counter_ns()
    result = search.simple_search(nums, target)
    end = time.perf_counter_ns()
    elapsed_time = end - start

    print(f"The amount of time that it took using simple search = {elapsed_time:,}")


    if result != -1:
        print(f"Found {target} at index {result}")
    
    else:
        print("Error, the value that you were looking for wasn't found in the list :(")


    # 2. Binary Search

    # Binary search, a searching algorithm that runs O(log2 n), is a searching alg-
    # orithm that begins checking the middle number in the array or list, and eli-
    # minate half the remaining numbers everytime.

    start = time.perf_counter_ns()
    result = search.binary_search(nums, target)
    end = time.perf_counter_ns()
    elapsed_time = end - start

    print(f"The amount of time that it took using binary search = {elapsed_time:,}")

    if result != -1:
        print(f"Found {target} at index {result}")
    
    else:
        print("Error, the value that you were looking for wasn't found in the list :(")



if __name__ == '__main__':
    main()