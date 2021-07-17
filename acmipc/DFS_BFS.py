''' 백준 1260번 문제 '''
from collections import deque


N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for i in range(N + 1)]  # n + 1 하는 이유 : 0번 인덱스부터 하면 헷갈리니까 맞추려고
graph

for _ in range(M):
    # 양방향 노드 연결 하기
    m1, m2 = map(int, input().split())  
    graph[m1][m2] = 1 
    graph[m2][m1] = 1 
    
''' BFS : 너비 우선 탐색 '''
def bfs(v):
    queue = [v] # 방문해야할 할 정점 저장
    visited[v] = 0 # 방문한 점은 0으로 표시
    
    while queue:
        v = queue.pop(0) # pop() 대신 pop(0)을 사용하면 큐가 됨
        print(v, end = " ")
        
        for i in range(1, n+1):
            if (visited[i] == 1) and (graph[v][i] == 1):
                queue.append(i)
                visit[i] = 0

''' DFS : 깊이 우선 탐색 '''
def dfs(v):
    visited[v] = 1 # 방문한 점은 1로 표시
    print(v, end = " ")
    
    for i in range(1, n+1):
        if (visited == 0) and (graph[v][i] == 1):
            dfs(i) # 재귀


        
        