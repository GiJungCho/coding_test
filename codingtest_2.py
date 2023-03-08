line_data, input_data , N = ([1, 2, 3, 4, 5], [0, 1, 1, 3, 2], 5)

out_put = ""
out_put_list = []

for i in range(N):
    if i == 0:
        out_put = out_put + str(i+1)
        out_put_list.insert(0,i+1)
    else:
        out_put = out_put[input_data[i-1] + len(out_put)] +str(i + 1)
        out_put_list.insert(input_data[i-1] + len(out_put),i+1)
print(out_put)
print(out_put_list)