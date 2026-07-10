import sys
import threading
from collections import deque

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))

    g = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = int(next(it))
        v = int(next(it))
        g[u].append(v)
        g[v].append(u)

    if N == 1:
        print("0")
        print("1")
        return

    reach = [False] * (N + 1)
    q = deque()
    q.append(1)
    reach[1] = True

    while q:
        u = q.popleft()
        for v in g[u]:
            if not reach[v]:
                reach[v] = True
                q.append(v)

    if not reach[N]:
        print("-1")
        return

    class PathState:
        __slots__ = ("path", "visitedMask")
        def __init__(self, path, visitedMask):
            self.path = path
            self.visitedMask = visitedMask

    beamWidth = 10000
    beam = [PathState([1], 1 << 0)]

    bestLen = -1
    bestPath = []

    while beam:
        nextBeam = []

        for state in beam:
            u = state.path[-1]
            if u == N:
                if len(state.path) > bestLen:
                    bestLen = len(state.path)
                    bestPath = state.path[:]
                continue

            for v in g[u]:
                bit = 1 << (v - 1)
                if state.visitedMask & bit:
                    continue
                new_path = state.path + [v]
                new_mask = state.visitedMask | bit
                nextBeam.append(PathState(new_path, new_mask))

        nextBeam.sort(key=lambda s: (-len(s.path), s.visitedMask, s.path[-1]))

        ptr = 0
        for i in range(len(nextBeam)):
            if i == 0:
                continue
            if nextBeam[ptr].visitedMask == nextBeam[i].visitedMask and nextBeam[ptr].path[-1] == nextBeam[i].path[-1]:
                continue
            ptr = ptr + 1
            nextBeam[ptr] = nextBeam[i]

        while len(nextBeam) > beamWidth:
            nextBeam.pop()

        beam = nextBeam

    if bestLen == -1:
        print("-1")
    else:
        print(bestLen - 1)
        print(" ".join(map(str, bestPath)))


if __name__ == "__main__":
    main()
