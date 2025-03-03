# Sorting
# Given an array A of N integers, check if it's a permutation
# (contains all numbers from 1 to N exactly once).

def is_permutation(A):
    return int(set(A)==set(range(1,len(A)+1)))

print(is_permutation([4,1,3,2]))
print(is_permutation([4,1,3]))