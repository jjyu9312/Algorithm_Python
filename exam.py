'''
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
'''

listA = [[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5],  
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
listB = [1,2,3,4,5]

for i in listA:
    print(i)
    for a, b in zip(i, listB):
        print()

def solution(answers):
    answer = []
    
    while True:
        
    return answeb