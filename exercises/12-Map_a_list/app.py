Celsius_values = [-2,34,56,-10]


 
# the magic go here:
def fahrenheit_values(x):
    return ((x * 9/5) + 32)
    
result = list(map(fahrenheit_values, Celsius_values))
print(result)
