import sys
from functools import lru_cache

sys.setrecursionlimit(10000)

@lru_cache(maxsize=None)
def compute_nim_value(x):
    if x == 0:
        return 0
    
    b_len = x.bit_length()
    base = 1 << (b_len - 1)
    modulus = b_len + 1
    
    target = base + (x - base) % modulus
    
    if x > target:
        return compute_nim_value(target)
    
    reachable = {compute_nim_value(x - step) for step in range(1, b_len + 1)}
    
    mex = 0
    while mex in reachable:
        mex += 1
        
    return mex

def main():
    content = sys.stdin.read().split()
    if not content:
        return

    data = map(int, content)
    _ = next(data) 
    
    nim_sum = 0
    for pile in data:
        nim_sum ^= compute_nim_value(pile)

    sys.stdout.write("Dat" if nim_sum > 0 else "Phu")

if __name__ == "__main__":
    main()
