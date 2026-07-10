def dist2(p, q):
    return (p[0] - q[0])**2 + (p[1] - q[1])**2

def closest_pair(points):
    points.sort()
    
    def solve(pts):
        n = len(pts)
        if n <= 3:
            best = float('inf')
            for i in range(n):
                for j in range(i + 1, n):
                    best = min(best, dist2(pts[i], pts[j]))
            return best
        
        mid = n // 2
        midx = pts[mid][0]
        
        d = min(solve(pts[:mid]), solve(pts[mid:]))
        
        strip = []
        for p in pts:
            if (p[0] - midx)**2 < d:
                strip.append(p)
        
        strip.sort(key=lambda x: x[1])
        
        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if (strip[j][1] - strip[i][1])**2 >= d:
                    break
                d = min(d, dist2(strip[i], strip[j]))
        return d
    
    return solve(points)

import sys
input = sys.stdin.readline

n = int(input().strip())
points = [tuple(map(int, input().split())) for _ in range(n)]

print(closest_pair(points))
