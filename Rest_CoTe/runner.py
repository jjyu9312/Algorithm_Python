'''
participant	completion	return
["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"

'''

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

def solution(participant,completion):
    # 참가자와 완주자를 알파벳 순으로 정렬 
    participant.sort()
    completion.sort()

    # python 내장함수인 zip을 이용해서 참가자와 완주자를 하나씩 비교 (완주자 개수까지)
    for p, c in zip(participant, completion) :
        if p != c :
            return p
    
    # 만약 참가자와 완주자가 모두 같다면 참가자의 마지막 선수를 리턴
    return participant.pop()

solution(participant, completion)    
