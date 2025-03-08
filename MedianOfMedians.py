def median_of_medians(arr, k):
    """
    Select the k-th smallest element from arr using the median of medians algorithm.

    :param arr: The list of elements
    :param k: The index of the element to find (0-based index)
    :return: The k-th smallest element in the list
    """

    def partition(arr, pivot):
        """ Helper function to partition the array around the pivot """
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        middle = [x for x in arr if x == pivot]
        return left, middle, right

    def select(arr, k):
        """ Helper function to recursively select the k-th smallest element """
        if len(arr) <= 5:
            return sorted(arr)[k]

        # Step 1: Divide the list into groups of 5
        groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]

        # Step 2: Find the medians of each group
        medians = [sorted(group)[len(group) // 2] for group in groups]

        # Step 3: Find the pivot (the median of the medians)
        pivot = select(medians, len(medians) // 2)

        # Step 4: Partition the array around the pivot
        left, middle, right = partition(arr, pivot)

        # Step 5: Determine which side to recurse on
        if k < len(left):
            return select(left, k)
        elif k < len(left) + len(middle):
            return middle[0]
        else:
            return select(right, k - len(left) - len(middle))

    return select(arr, k)


# Example usage:
arr = [10, 4, 5, 5, 8, 6, 11, 26]
k = 3  # Find the 3rd smallest element (index 2)
result = median_of_medians(arr, k)
print(f"The {k + 1}-th smallest element is: {result}")
