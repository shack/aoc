import heapq

def L1(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

# Parameters:
# - start: tuple of coordinates
# - valid_coords: set of tuples of coordinates that can be stepped on
def astar(start, valid_coords, heur=lambda _: 0):
    q = []
    visited = { start: 0 }
    src = {}
    heapq.heappush(q, (heur(start), start))
    while q:
        h, curr = heapq.heappop(q)
        c = h - heur(curr)
        if curr in visited and visited[curr] < c:
            continue
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            np = (curr[0] + dx, curr[1] + dy)
            if np in valid_coords:
                new_c = c + 1
                new_h = new_c + heur(np)
                if np not in visited or visited[np] > new_c:
                    src[np] = curr
                    visited[np] = new_c
                    heapq.heappush(q, (new_h, np))
    return visited, src

def get_path(src, start, end):
    p = []
    while end != start:
        p.append(end)
        n = src[end]
    p.append(start)
    return p[::-1]

def rotate_ccw(dx, dy):
    return -dy, dx