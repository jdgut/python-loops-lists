#Import random
import random

#Create the function below:
def matrixBuilder(number):
    matrix = list()
    for i in range(number):
        row = list()
        for y in range(number):
            row.append(1)
        matrix.append(row)
    
    return matrix

rand_number = random.randint(1,10)
print(matrixBuilder(rand_number))