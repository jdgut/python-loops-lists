parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot(parking_info):
    state = { "totalSlots": 0, "availableSlots": 0, "occupiedSlots": 0}
    for i in range(len(parking_info)):
        row = parking_info[i]
        for y in row:
            if y == 1:
                state['occupiedSlots'] = state['occupiedSlots'] + 1
                state['totalSlots'] = state['totalSlots'] + 1
            elif y == 2:
                state['availableSlots'] = state['availableSlots'] + 1
                state['totalSlots'] = state['totalSlots'] + 1
    
    return state

print(get_parking_lot(parking_state)) 