# BFS - 너비 우선 탐색

from collections import deque
''' 양방향에서 탐색할 수 있는 deque 이용 '''

def solution(n, edge):
    routes = dict() # 딕셔너리에 노드 별 연결 정보 저장
    for e1, e2 in edge:
        routes.setdefault(e1, []).append(e2) # setdefault(키, 인자)
        routes.setdefault(e2, []).append(e1) # deque에 [노드 번호, 깊이] 정보를 한번에 삽입
        
    q = deque([[1, 0]]) # [노드 번호, 깊이]
    check = [-1] * (n+1) # -1로 초기화, 인접 노드를 탐색할 때는 한번 deque에 넣은 노드는 0으로 체크 
    while q:
        index, depth = q.popleft() # 왼쪽부터 하나씩 제거 후 반환
        check[index] = depth
        
        
def my_sol(n, edges):
    graph = [[] for i in range(n+1)]

    for i in range(len(edges)):
        if edges[i][1] not in graph[i]:
            graph[edges[i][0]].append(edges[i][1])

        if edges[i][0] not in graph[i]:
            graph[edges[i][1]].append(edges[i][0])

    print("Graph: ", graph, "\n")



    """
    이 위로는 데이터 준비 과정
    이 밑으로는 너비 우선 탐색을 통해 dist 배열에 값 채워넣는 과정
    """
    
    start = 1
    queue = [start]
    dist = [0] * (n+1)
    dist[0] = -1
    dist[start] = -1
    count = 1

    # 1번 노드와 다른 노드와의 거리에 대한 값을 갖는 dist 배열에 0이 없을 때까지 반복한다.
    # 이는 1과 연결된 모든 노드를 방문한다는 뜻이다.
    while 0 in dist:
        # new_arr 배열은 다음 단계에 탐색할 노드들을 저장하기 위한 배열이다.
        new_arr = []

        # queue에 담겨 있는 노드들마다 bfs를 한다. 즉, 시작 노드에서 갈 수 있는 노드들을 방문한다.
        # 처음 반복을 시작할 때는 [1]이므로, start는 1이다.
        print("시작하는 큐: ", queue)
        for start in queue:
            print("탐색을 시작하는 노드: ", start)

            # start에서 갈 수 있는 노드들을 탐색한다. start가 1인 경우, cand는 3, 2 이다.
            for cand in graph[start]:
                
                # dist[cand]는 1번 노드와의 거리를 나타낸다. 이 값이 0이라면, 아직 방문되지 않은 것이다.
                # 따라서, dist[cand]의 값을 count만큼 증가시키고, new_arr 배열에 append한다.
                if dist[cand] == 0:
                    print("bfs로 탐색한 노드: ", cand)
                    dist[cand] += count
                    new_arr.append(cand)
        print("새로 만들어진 큐: ", new_arr, "\n")
        count += 1
        queue = new_arr

    print("dist: ", dist, "\n")
    return dist.count(max(dist))


edges = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6
print("정답: ", my_sol(n, edges))

def bfs(v, visited, adj):

    count = 0

    q = list([[v, count]])
    print("q : ", q)
    
    while q:
        # print(v, visited, adj,q)
        value = q.pop(0)
        print("value : ", value)
        
        v = value[0]
        print("v : ", v)
        
        count = value[1]
        print("count : ", count)
        
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for e in adj[v]:
                print("e : ", e)
                q.append([e, count])

def solution(n, edge):
    node = [[] for _ in range(n + 1)]
    dist_list = [-1] * (n + 1)

    for e in edge:
        node[e[0]].append(e[1])
        node[e[1]].append(e[0])

    bfs(1, dist_list, node)

    return dist_list.count(max(dist_list))
    
    
solution(n, edges)