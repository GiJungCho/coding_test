scoville, K = ([1,2,3,4,5,6,7,8,8,9], 9)
# scoville,K = ([1, 2, 6, 9, 10, 12], 7) # 2

# scoville,K = ([1, 2, 6, 7, 9, 10, 12,6,6,6], 7)
def return_Scorvill_mix(a, b):
    return a + (b * 2)


def solution(scoville, K):
    answer = 0

    while True:
        scoville.sort()
        if(len(scoville) <= 1) == False:

            if min(scoville) < K:

                scoville.insert(0,return_Scorvill_mix(scoville[0],scoville[1]))
                scoville.remove(scoville[1])
                scoville.remove(scoville[2])
                answer += 1

                print(scoville)
            else:
                return answer - 1

        else:
            return -1


print(solution(scoville, K))