# Program 2: Divide and Conquer

- [ ] A paragraph describing the approach you will use to solve the problem. Provide at least 2 illustrations that explain the
approach.
- [ ] High-level pseudocode for an algorithm that uses that rule to solve the computational problem for any input
- [ ] An explanation and justification for why your algorithm is correct (1-3 paragraphs)
- [X] A table of your test cases, the answers you expect, and the answers returned by running your implementation of the
algorithm.
- [ ] The derivation of a recurrence relation describing the run time in terms of the number of points n. (Show your work!)
You may assume that the random pivot divides the elements in half each time.
- [ ] A solution to the recurrence relation (show your work). Ideally, you will get a run time in terms of O (n) in asymptotic
notation.
- [ ] A table and graph from benchmarking different lists with different sizes and values of k. Benchmark your implementation
versus an approach that sorts the numbers and picks the element at index k − 1. If the benchmarks do not support your
theoretically-derived run time and/or do not provide evidence that the run time of your algorithm grows more slowly than the sorting approach,
this may indicate a flaw in your implementation.
- [ ] An appendix containing all of your source code and test cases.

# Report
## Approach to solving the problem


### Illustration 1: 

### Illustration 2:

## Pseudocode
```psuedocode
PROCEDURE SELECTION(A, k):
    RETURN SELECTION_RECURSIVE(A, k - 1)

PROCEDURE SELECTION_RECURSIVE(A, k):
    IF LENGTH(A) <= 5 THEN
        RETURN SORT(A)[k]
    END IF

    sublists ← EMPTY LIST
    FOR i FROM 0 TO LENGTH(A) - 1 STEP 5 DO
        sublist ← SUBARRAY(A, i, MIN(i + 5, LENGTH(A))) 
        sublists.APPEND(sublist)
    END FOR

    medians ← EMPTY LIST
    FOR EACH sublist IN sublists DO
        sorted_sublist ← SORT(sublist)
        median_index ← FLOOR(LENGTH(sorted_sublist) / 2)
        median_value ← sorted_sublist[median_index]
        APPEND median_value TO medians
    END FOR

    pivot ← SELECTION_RECURSIVE(medians, FLOOR(LENGTH(medians) / 2))

    (left, middle, right) ← PARTITION(A, pivot)

    IF k < LENGTH(left) THEN
        RETURN SELECTION_RECURSIVE(left, k)
    ELSE IF k < LENGTH(left) + LENGTH(middle) THEN
        RETURN middle[0]
    ELSE
        new_k ← k - LENGTH(left) - LENGTH(middle)
        RETURN SELECTION_RECURSIVE(right, new_k)
    END IF
END FUNCTION

PROCEDURE PARTITION(A, pivot):
    left ← EMPTY LIST
    middle ← EMPTY LIST
    right ← EMPTY LIST

    FOR EACH element IN A DO
        IF element < pivot THEN
            left.APPEND(element)
        ELSE IF element = pivot THEN
            middle.APPEND(element)
        ELSE IF element > pivot THEN
            right.APPEND(element)
        END IF
    END FOR

    RETURN (left, middle, right)
END FUNCTION
```

## Test cases
| Input                           | Expected Output | Actual Output |
|---------------------------------|-----------------|---------------|
| [1, 2, 3, 4, 5], k=1            | 1               | 1             |
| [1, 2, 3, 4, 5], k=3            | 3               | 3             |
| [1, 2, 3, 4, 5], k=5            | 5               | 5             |
| [5, 4, 3, 2, 1], k=1            | 1               | 1             |
| [5, 4, 3, 2, 1], k=3            | 3               | 3             |
| [5, 4, 3, 2, 1], k=5            | 5               | 5             |
| [2, 2, 2, 1, 1, 3, 3], k=1      | 1               | 1             |
| [2, 2, 2, 1, 1, 3, 3], k=5      | 2               | 2             |
| [2, 2, 2, 1, 1, 3, 3], k=7      | 3               | 3             |
| [7, 7, 7, 7, 7], k=1            | 7               | 7             |
| [7, 7, 7, 7, 7], k=3            | 7               | 7             |
| [7, 7, 7, 7, 7], k=5            | 7               | 7             |
| [42], k=1                       | 42              | 42            |
| [-10, 5, -3, 0, 8, -7, 12], k=1 | -10             | -10           |
| [-10, 5, -3, 0, 8, -7, 12], k=3 | -3              | -3            |
| [-10, 5, -3, 0, 8, -7, 12], k=7 | 12              | 12            |
| [10, 9, 8, 7, 6, 5], k=3        | 7               | 7             |
| [5, 4, 3, 2, 1], k=3            | 3               | 3             |
| [3, 2, 1], k=2                  | 2               | 2             |

## Recurrence relation of run time

## Solution to the recurrence relation

## Benchmarking results

## Appendix
```python
# Your source code here
```
```python
# Your test cases here
```
```python
# Your benchmarking code here
```
```python
# Your benchmarking results here
```
