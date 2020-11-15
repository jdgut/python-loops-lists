people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    newlist = list()
    for i in people:
        if i != person_name:
            newlist.append(i)

    return newlist

print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))