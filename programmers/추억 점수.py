
def solution(name, yearning, photo):
    answer = []
    hashmap = dict()
    for i, v in zip(name, yearning):    # hashmap = {i:v for i, v in zip(name, yearning)}
        hashmap[i] = v
    count = 0
    for pho in photo:
        for p in pho:
            if p in hashmap.keys():
                count += hashmap[p]
        answer.append(count)
        count = 0

    return answer