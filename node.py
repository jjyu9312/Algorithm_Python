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


from collections import deque


def solution(n, edge):
    answer = 0
    route = [0]*(n+1) #노드 1부터 각 노드까지의 거리
    edge.sort() #노드 1부터 연결 정보 확인하기 위해 정렬
    queue = deque() 
    graph = [[] for i in range(n+1)] #각 노드에 연결된 노드 정보 저장
    
    for e in edge: # 양방향이므로 
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    queue.append(1)
    route[1] = 1
    
    while queue:
        now = queue.popleft()
        for g in graph[now]:
            if route[g]==0:
                queue.append(g)
                route[g] = route[now]+1
        
    # 1번 노드로부터 가장 멀리 떨어진 노드 개수 계산
    max_edge= max(route)
    for r in route:
        if r == max_edge:
            answer+=1     
            
    return answer