my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:
# average = sum(my_list) / len(my_list)

average = 0
for i in my_list:
    average = average + i

print(average / len(my_list))
