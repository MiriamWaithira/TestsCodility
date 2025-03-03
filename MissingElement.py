# counting
# An array contains N integers from 1 to N+1, but one number is missing.
# Find the missing number.
def missing_element(A):
    N= len(A)+1
    expected_sum = N*(N+1)//2
    return expected_sum-sum(A)

print(missing_element([2,1,3,5]))