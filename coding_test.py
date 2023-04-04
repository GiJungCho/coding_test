scoville,K = ([1, 2, 6, 7, 9, 10, 12,6,6,6], 7)

def solution(scoville, K):
    scoville.sort()
    answer = 0

    for i, v in enumerate(scoville):
        if i == 0:
            continue
        if v <= K:
            compare = [scoville[i - 1], v]
            compare.sort()
            a = compare[0] + compare[1] * 2
            scoville[i] = a
            answer += 1
            # print(a, v)
            if a >= K:
                break
    print(scoville)
    if scoville[-1] < K:
        answer = -1

    return answer

print(solution(scoville, K))