chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    # return list1 + list2
    for i in list2:
        list1.append(i)
    
    return list1
    
print(merge_list(chunk_one, chunk_two))
