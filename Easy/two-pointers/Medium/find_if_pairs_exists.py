# 1. Constant Time complexity nlog(n) - Using binary search
# 2. Using extra space set or dict - O(n)
# 3. Two pointer approach - only if sorted

# Best in time is hashing
# Best in space is 2 pointers

# 2 pointer approach
# Find if a pair exists with the given sum in the given sorted list.

def check_pair(A, B):
    start = 0
    end = len(A) - 1
    while start < end:
        if A[start] + A[end] == B:
            return True
        elif A[start] + A[end] > B:
            end -= 1
        else:
            start += 1
    return False


if __name__ == '__main__':
    A = [-3, 0, 1, 3, 6, 7, 12, 14, 18, 25]
    B = 17
    print(check_pair(A, B))