# You are given a sorted array A of size N and a target value B.
# Your task is to find the index (0-based indexing) of the target value in the array.

# If the target value is present, return its index.
# If the target value is not found, return the index of least element greater than equal to B.
# Your solution should have a time complexity of O(log(N)).

def solution(A, B):
    start = 0
    ans = 0
    end = len(A) - 1

    while(start <= end):
        mid = (start + end) // 2

        if A[mid] == B:
            return mid
        elif A[mid] < B:
            ans = mid + 1
            start = mid + 1
        else:
            end = mid - 1
    return ans 

if __name__ == "__main__":
    A = [1, 3, 5, 6]
    B = 5
    print(solution(A, B))