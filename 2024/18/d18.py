import copy
import heapq

input = [ l.strip() for l in open(0) ]
input = [ tuple(map(int, l.split(','))) for l in input ]
N = 71
m = []
for i in range(N):
    m.append(list('.' * N))

def fall(m, n):
    for (x, y), _ in zip(input, range(n)):
        m[y][x] = '#'

def L1(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

# adapted from: https://code.activestate.com/recipes/578919-python-a-pathfinding-with-binary-heap/
def astar(array, start, goal, neighbors=[(0, 1), (1, 0), (-1, 0), (0, -1)], heuristic=L1):
    X, Y = len(array[0]), len(array)
    visited = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    q = []

    heapq.heappush(q, (fscore[start], start))

    while q:
        _, curr = heapq.heappop(q)

        if curr == goal:
            path = []
            while curr in came_from:
                path.append(curr)
                curr = came_from[curr]
            return path

        visited.add(curr)
        x, y = curr
        for dx, dy in neighbors:
            neighbor = nx, ny = x + dx, y + dy
            neighbor_g_score = gscore[curr] + heuristic(curr, neighbor)
            if not (0 <= nx < X) or not (0 <= ny < Y) or array[ny][nx] == '#':
                continue

            if neighbor in visited and neighbor_g_score >= gscore.get(neighbor, 0):
                continue

            if neighbor_g_score < gscore.get(neighbor, 0) or neighbor not in gscore:
                came_from[neighbor] = curr
                gscore[neighbor] = neighbor_g_score
                fscore[neighbor] = neighbor_g_score + heuristic(neighbor, goal)
                heapq.heappush(q, (fscore[neighbor], neighbor))
    return None

# pt1
w = copy.deepcopy(m)
for (x, y), _ in zip(input, range(1024)):
    w[y][x] = '#'
print(len(astar(w, (0, 0), (N - 1, N - 1))))

# pt2
for i in range(len(input)):
    if not astar(m, (0, 0), (N - 1, N - 1)):
        print(input[i - 1])
        break
    x, y = input[i]
    m[y][x] = '#'