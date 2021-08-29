food_times = [3, 1, 2]

times = {}
for idx, time in enumerate(food_times):
    if time in times:
        times[time].append(idx)
    else:
        times[time] = [idx]
        
times
times.sorted
len_foods = len(food_times)
cycle = 0

for time in sorted(times):
    if k - (len_foods*(time-cycle)) >= 0:
        k -= len_foods*(time-cycle)
        len_foods -= len(times[time])
        cycle += time-cycle
    else:
        k %= len_foods
        for i in times:
            if i >= time:
                idx = times[i][0]
                break
        for i in range(idx, len(food_times)):
            if food_times[i] >= time:
                if k == 0:
                    return i+1
                k -= 1
                
            

from itertools import cycle

def solution(food_times, k):
    index_array = cycle([i for i in range(len(food_times))])
    done = False
    counter = 0
    while done is False:
        index = next(index_array)
        if sum(food_times) == 0:
            return -1
        if food_times[index] > 0:
            counter += 1
            food_times[index] -= 1
        done = True if counter == k+1 else False
    return index + 1

ndex_array = cycle([i for i in range(len(food_times))])

for i in ndex_array:
    i
    
