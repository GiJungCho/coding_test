N, bell_data = (3,
 [[1, 2, 1, 1, 1, 2, 2, 1],
  [1, 1, 1, 1, 1, 1],
  [2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1]])

data = bell_data[2] # @ 지우기

def fun_2(data):
    cheak_1_data = []
    cheak_2_data = []
    sum_result = 0
    before_data = [0]

    for i in range(len(data)):

        now_data = data[i]
        if i == 0: # 첫번쨰 for문의 경우
            before_data = [now_data]

        elif now_data == before_data[0]: # 현재 데이터가 같다면
            before_data.append(now_data)



        if i != 0 and before_data[0] != now_data: # @@ == else라고 해도 되나?
            if before_data[0] == 1: # 1번 풍선
                cheak_1_data = before_data
                before_data = [now_data]

                if len(cheak_1_data)>0 and len(cheak_2_data)>0 :# 둘다 0 이상의 경우
                    sum_result = sum_result + min(len(cheak_1_data),len(cheak_2_data))

                    cheak_1_data = [] # 초기화
                    cheak_2_data = []

            elif before_data[0] == 2: # 2번 풍선의 경우
                cheak_2_data = before_data
                before_data = [now_data]

                if len(cheak_1_data)>0 and len(cheak_2_data)>0 :# 둘다 0 이상의 경우
                    sum_result = sum_result + min(len(cheak_1_data),len(cheak_2_data))

                    cheak_1_data = [] # 초기화
                    cheak_2_data = []

    return int(sum_result * 2)

result = fun_2(data)
print(result)