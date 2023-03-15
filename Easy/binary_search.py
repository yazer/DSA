def binary_search(A, B):
    start = 0
    end = len(A) - 1

    while(start <= end):
        mid = (start + end) // 2
        if A[mid] == B:
            return mid
        elif A[mid] < B:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    B = 7
    print(binary_search(A, B))