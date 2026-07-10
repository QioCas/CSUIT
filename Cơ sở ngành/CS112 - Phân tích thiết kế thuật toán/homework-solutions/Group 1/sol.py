import sys

def solve():
    it = iter(sys.stdin.buffer.read().split())
    try:
        n = int(next(it)); m = int(next(it))
    except StopIteration:
        return

    first = {}
    for i in range(n):
        x = int(next(it))
        first.setdefault(x, i)

    b = [int(next(it)) for _ in range(m)]

    limit = n
    for x in reversed(b):
        p = first.get(x)
        if p is None or p > limit:
            limit = n
        else:
            limit = p

    sys.stdout.write("Alice\n" if limit < n else "Bob\n")

if __name__ == "__main__":
    solve()