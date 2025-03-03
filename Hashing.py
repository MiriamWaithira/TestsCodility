# Odd occurrences in an array
# An array consists of integers taht occur twice, except one.
# Finding the element that appears only once
def odd_occurrence(A):
    result = 0
    for num in A:
        result ^=num #To cancel out the numbers that occur more than once
    return result
    
print(odd_occurrence([9,3,9,3,9,7,9])) #Only 7 appears once