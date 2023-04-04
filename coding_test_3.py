scoville, K = ([1,2,3,4,5,6,7,8,8,9], 9)
# scoville,K = ([1, 2, 6, 9, 10, 12], 7) # 2

# scoville,K = ([1, 2, 6, 7, 9, 10, 12,6,6,6], 7)
def return_Scorvill_mix(a, b):
    return a + (b * 2)


def solution(scoville, K):
    answer = 0
    while True:
        print(scoville)
        if min(scoville) < K and (len(scoville) <= 1) == False:  # k 보다 다 커야함

            scoville_min_1 = min(scoville)
            scoville.remove(scoville_min_1)

            scoville_min_2 = min(scoville)
            scoville.remove(scoville_min_2)

            scoville.append(return_Scorvill_mix(scoville_min_1, scoville_min_2))
            answer = answer + 1

        elif len(scoville) <= 1:  # 스코빌 지수가 다 안나온다면
            return -1

        else:
            return answer


print(solution(scoville, K))