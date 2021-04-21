'''
n	vertex	                                                   return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3
'''

'''
제한사항
노드의 개수 n은 2 이상 20,000 이하입니다.
간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
'''

from collections import deque

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

answer = 0
route = [-1] * (n + 1)
print(route)

vertex.sort()
vertex

queue = deque([])
graph = [[] for _ in range(n+1)]

# 양방향 표시
for e in vertex:
    graph[e[0]].append(e[1])
    graph[e[1]].append(e[0])
    print(graph)
queue.append(1)    
route[1] = 1

print(queue)
print(route)

while queue:
    v = queue.popleft()
    for i in graph[v]:
        if route[i] == -1:
            queue.append(i)
            print(queue)
            route[i] = route[v] + 1
            print(route)

max_edge = max(route)
print(max_edge)

for r in route:
    if r == max_edge:
        answer += 1

print(answer)
1