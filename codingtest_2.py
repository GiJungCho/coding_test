# N = int(input())
# data = [1 for i in range(N)]
# lost = list(map(int,input().split()))
# reserve = list(map(int,input().split()))
def solution(N, lost, reserve):
    data = [1 for i in range(N)]
    for i in range(len(data)):
        if (i+1 in reserve):  # reserve 데이터의 인덱스와 같다면 == 데이터에 접근할 수 있다면,
            data[i]= data[i] + 1
        if (i+1 in lost):
            data[i]= data[i] - 1

    for i in range(len(data)):
        if data[i] == 0 :
            try: # 앞에 데이터에서 먼저 가져 올 수 있따면 가져오고
                if data[i - 1] == 2 and data[i] == 0 and i != 0 : # 2의 경우 - 1, 현재 셀은 + 1 # 음수로 맨 마지막을 호출하면 안됨!
                    data[i - 1] = data[i - 1] - 1
                    data[i] = data[i] + 1
            except:
                try:# 앞에 데이터에서 못 가져오면 뒤의 데이터에서 가져온다.
                    if data[i + 1] == 2 and data[i] == 0 : # 2의 경우 - 1
                        data[i + 1] = data[i + 1] + 1
                        data[i] = data[i] + 1
                except:
                    pass
    result = [1 for i in range(N)  if data[i] == 1 or data[i] == 2]
    return int(sum(result))
# print(solution(N, lost, reserve))
print(solution(N = 5, lost = [1,2], reserve = [4,5]))
