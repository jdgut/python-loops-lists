list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(all_numbers):
    even_list = list()
    odd_list = list()

    for i in all_numbers:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return [ odd_list, even_list ]

print(merge_two_list(list_of_numbers))

