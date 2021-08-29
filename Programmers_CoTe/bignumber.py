''' N : 숫자 개수, M : 숫자가 더해지는 횟수, K : 최대 반복 횟수 '''


# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# 1
result = 0

while True:
    for i in range(k):
        if m == 0: 
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# 2 
m = 8; k = 3
count = int(m / (k+1)) * k # 큰 수가 더해지는 개수
count += m % (k+1) # 나누어 떨어지지 않을 때 큰 수 한번 더 추가

result = 0
result += count * first
result += (M - count) * second
print(result)

