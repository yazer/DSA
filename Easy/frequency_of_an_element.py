# Find the frequency of an element in a list

def freq_element(A, B):
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == B:
            left_idx = mid
            end = mid - 1
        elif A[mid] < B:
            start = mid + 1
        else:
            end = mid - 1

    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == B:
            right_idx = mid
            start = mid + 1
        elif A[mid] < B:
            start = mid + 1
        else:
            end = mid - 1
    return right_idx - left_idx + 1


if __name__ == "__main__":
    A = [1, 2, 2, 3, 4, 4, 4, 4, 4, 5]
    B = 4
    print(freq_element(A, B))