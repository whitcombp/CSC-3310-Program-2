# ref: https://gist.github.com/boulethao/a15809963d326a5ad43f255fbffbf9ff#file-medianofmedians-png
def selection(A : list, k : int):
    return selection_recursive(A, k - 1)

def selection_recursive(A : list, k : int):
    if len(A) <= 5:
        return sorted(A)[k]
    sublists = [A[i:i + 5] for i in range(0, len(A), 5)]
    medians = []
    for sublist in sublists:
        medians.append(sorted(sublist)[len(sublist) // 2])
    pivot = selection_recursive(medians, len(medians) // 2)

    left, middle, right = partition(A, pivot)
    if k < len(left):
        return selection_recursive(left, k)
    elif k < len(left) + len(middle):
        return middle[0]
    else: # k < len(left) + len(middle) + len(right)
        return selection_recursive(right, k - len(middle) - len(left))

def partition(A : list, pivot : int):
    left = []
    middle = []
    right = []
    for i in A:
        if i < pivot:
            left.append(i)
        if i == pivot:
            middle.append(i)
        if i > pivot:
            right.append(i)
    return (left, middle, right)



def main():
    numbers = [1, 2, 2, 2, 3, 4, 8, 6, 7, 3]
    s = selection(numbers, 10)
    print(s)

if __name__ == "__main__":
    main()