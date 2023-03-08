x_max,y_max, N, data = (10, 5, 3, [[1, 4], [3, 2], [2, 8], [2, 3]])

for i in range(len(data)): #방향 때문에 위에서 아래로 셈
    if data[i][0] == 3 or data[i][0] == 4:
        data[i][1] = int(y_max - data[i][1])

# 여기서 역배열로 서칭할 것인지 정배열로 서칭할 것인지 고려.
direction = {}
#              반시계 시계방향
direction[4] = ["1_1", "2",int(y_max-1)] # east 동 4
direction[3] = ["2", "1_1",int(y_max-1)] # west 서 3
direction[2] = ["4", "3_1",int(x_max-1)] # south 남 2
direction[1] = ["3_1", "4",int(x_max-1)] # north 북 1

x_start , y_start = data[len(data)-1] # 맨 마지막 번호는 시작 지점.

dic = {} #사전 형태로 데이터 저장
for i in range(len(data)):
    dic[data[i][0],data[i][1]] = 1


def serch(now_driection, distance,wow , cheak_direction ):  # wow = 정방향 역방향

    if cheak_direction == 1:
        for i in range(-direction[now_driection][2], 0):
            i = abs(i)
            distance = distance + 1
            try:
                cheak_logic = dic[now_driection,i]
                return distance, int(direction[now_driection][wow][0]), wow, cheak_direction

            except:
                pass
    else:
        for i in range(0,direction[now_driection][2]):
            distance = distance + 1
            try:
                cheak_logic = dic[now_driection,i]
                return distance, int(direction[now_driection][wow][0]), wow, cheak_direction

            except:
                pass

    if (len(direction[now_driection][wow]) == 1):  # 정방향 역방향 =>wow
        cheak_direction = 1
    else:
        cheak_direction = 0

    serch(int(direction[now_driection][wow][0]), distance, wow, cheak_direction)# @@

while True:
    wow = 1 # 시계 방향 판단. 시계방향
    distance_1 = 0
    cheak_logic_1 = 0
    print(0,y_start)

    for i in range(0,y_start): # 반시계 방향
        distance_1 = distance_1 + 1
        try:
            cheak_logic_1 = dic[x_start,i]
            break
        except:
            pass


    if cheak_logic_1 == 0:

        if (len(direction[x_start][wow]) == 1): # 정방향 역방향 =>wow
            cheak_direction = 0 # 다음 정/역 방향 판단
        else:
            cheak_direction = 1 # 다음 정/역 방향 판단
        print(int(direction[x_start][wow][0]),distance_1,wow, cheak_direction)
        distance_1,aa,wow ,cheak_direction = serch(int(direction[x_start][wow][0]),distance_1,wow, cheak_direction)
    break

while True:
    wow = 0 # 시계 방향 판단. 반시계 방향
    distance_2 = 0
    cheak_logic_2 = 0
    print(y_start,x_max-1)

    for i in range(y_start,x_max-1): #시계 방향
        distance_2 = distance_2 + 1
        try:
            cheak_logic_2 = dic[x_start,i]
            break
        except:
            pass

    if cheak_logic_2 == 0:
        if (len(direction[x_start][wow]) == 1): # 정방향 역방향
            cheak_direction = 0 # 다음 정/역 방향 판단
        else:
            cheak_direction = 1 # 다음 정/역 방향 판단

        distance_2, aa, wow, cheak_direction = serch(int(direction[x_start][wow][0]), distance_2, wow, cheak_direction)
    break
print(distance_1,distance_2)
print((x_max -1 ) * 2 + (y_max - 1)* 2)
print(max(distance_1,distance_2))
print((x_max -1 ) * 2 + (y_max - 1)* 2 - max(distance_1,distance_2))
print((x_max -1 ) * 2 + (y_max - 1)* 2 - max(distance_1,distance_2))