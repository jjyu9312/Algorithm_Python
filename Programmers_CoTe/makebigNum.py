'''
number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"
'''

number = "4177252841"
print(len(number))
k = 4


def solution(number, k):
    answer = ''
    stack = []

    for i in number:
        while stack and stack[-1] < i and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)
    
    if k > 0:
        for i in range(k):
            stack.pop()
    
    answer = ''.join(stack)
    
    return answer
































