n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split())) # 리스트 변수에 입력 값 저장
    min_value = min(data)
    result = max(result, min_value)
    
k = 7
s = [1,2,3,4,5,6,7]

k, *s = list(map(int, input().split()))
print(k, s)

n, m, k = map(int, input().split())
print(n, m, k)
