# Arrays
# Given an array of N integers and an integer K, rotate the array K times to the right.
# Each rotation shifts elements right, moving the last element to the first position.

def cyclic_rotation(A, K):
    if not A:return A #to handle an empty array
    K = K % len(A) #to handle cases where K > len(A)
    return A[-K:]+A[:-K]

print(cyclic_rotation([3,8,9,7,6],3))