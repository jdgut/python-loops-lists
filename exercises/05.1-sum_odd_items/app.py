arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]
odds_total = 0
#Your code go here:
def isOdd(number):
    return number % 2 != 0

for i in arr: 
    if(isOdd(i)): odds_total+=i

print(odds_total)
