def lyrics_generator(beats):
    line = list()
    tracking1 = 0
    for el in beats:
        if el == 1:
            line.append('Drop the base')
            tracking1 += 1
        elif el == 0:
            line.append('Boom')

        if tracking1 == 3:
            line.append("!!!Break the base!!!")
            tracking1 = 0

    return ' '.join(line) + ' '

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))