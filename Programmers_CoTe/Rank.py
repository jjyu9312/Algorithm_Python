'''
제한사항
선수의 수는 1명 이상 100명 이하입니다.
경기 결과는 1개 이상 4,500개 이하입니다.
results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
모든 경기 결과에는 모순이 없습니다.
'''

'''
n	results	                                    return
5	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	2
'''

from collections import deque

n = 5
result = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
result.sort()
result

def solution(n, results):
    answer = 0
    return answer

stack = []

graph = [[] for _ in range(n+1)]

wins, loses = {}, {}

for i in range(n+1):
    wins[i], loses[i] = set(), set()

for i in range(n+1):
    for battle in results:
        if battle[0] == i: # i가 이긴 사람들
            wins[i].add(battle[1])
            print("wins : ", wins)
        if battle[1] == i: # i를 이긴 사람들
            loes[i].add(battle[0])
            print("loses : ", loses)
            
    for winner in loses[i]:
        wins[winner].update(wins[i])
    for loser in wins[i]:
        loses[loser].update(loses[i])
        

    cnt = 0
    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n-1:
            cnt += 1
    return cnt
    
