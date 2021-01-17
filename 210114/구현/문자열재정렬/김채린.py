arr='FIHJG98S4ND9G84H320011'

sort_arr=sorted(arr)
print(sort_arr)
# ['1', '5', '7', 'A', 'B', 'C', 'K', 'K']

arr_len=len(sort_arr)-1

for i in range(0,arr_len):
    if sort_arr[0].isdigit():
        #리스트 앞에꺼 팝해서 뒤에 붙여버리기~
        x=sort_arr.pop(0)
        sort_arr.append(x)


print(''.join(sort_arr))