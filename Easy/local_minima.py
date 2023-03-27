# Given an array of distinct numbers.
# Find any local minima in the array.
# An element smaller than all available neighbours

def local_minima(A):
  start = 0
  end = len(A) - 1

  if A[0] < A[1]:
    return A[0]
  if A[len(A) - 1] < A[len(A) - 2]:
    return A[len(A) - 1]

  while(start <= end):
    mid = (start + end)//2

    if A[mid] < A[mid - 1] and A[mid] < A[mid + 1]:
      return A[mid]
    elif A[mid] > A[mid - 1]:
      end = mid - 1
    else:
      start = mid + 1 


if __name__ == "__main__":
    A = [13, 6, 1, 0, 9, 15]
    print(local_minima(A))