number,k = '1231234',3

def fun_1(number,use_k,cheak_list, now_data = None): # 해당값과 필요없는 나머지 숫자 전부 리턴.

    for i,v in enumerate(number):
        v = number[i+1:]

        for j in range(len(v)):
            if now_data == None:
                now_data = number[i] + v[j]
            else:
                pass

            if len(now_data) == use_k:
                cheack_list.append(now_data)
            elif len(now_data) <= use_k:
                cheak_list = fun_1(list(set(v).difference(v[j])), use_k, cheak_list,now_data)
            else:
                continue

    return cheak_list

# def fun_2(V,now_data,cheack_list,d): # 현재 데이터,
#     for i in range(len(V)):
#         now_data = now_data + V[i]
#
#         if len(now_data) == use_k:
#             cheack_list.append(now_data)
#
#         elif len(now_data) <= use_k:
#             cheak_list = fun_2(list(set(v).difference(v[j])), use_k, cheak_list)
#
#         else:
#             continue
#
def solution(number,k):
    cheak_list = []
    use_k = len(number) - k


    answer = fun_1(number, use_k,cheak_list)
    return max(answer)

solution(number,k)