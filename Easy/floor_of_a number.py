# if the number is present return the number
# else return the greatest number which is less than the given number

def find_floor(A, B):
    start = 0
    end = len(A) - 1
    ans = -1000000

    while start <= end:
        mid = (start + end) // 2

        if A[mid] == B:
            return A[mid]
        elif A[mid] < B:
            ans = A[mid]
            start = mid + 1
        else:
            end = mid - 1
    return ans

if __name__ == "__main__":
    A = [1, 2, 4, 5]
    B = 3
    print(find_floor(A, B))