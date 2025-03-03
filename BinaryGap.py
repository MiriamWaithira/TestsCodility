def binary_gap(N):
    binary_str = bin(N)[2:]
    gaps = binary_str.strip('0').split('1')
    return max(map(len, gaps), default=0)

print(binary_gap(9))
print(binary_gap(529))