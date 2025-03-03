# Frog Jump
# A frog wants to jump across a river.It starts at position X and wants to reach Y.
# It can jump D units ata atime. Minimum no. of jumps required?
# X=10,Y=85,D=30
def frog_jump(X,Y,D):
    return (Y-X + D-1) // D

print(frog_jump(10,85,30))