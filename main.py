def factOrSum(x,y):

    bazinga = 0

    if y == "sum":
        for i in range(0, x+1): 
            bazinga = bazinga + i
    
    else:
        bazinga = 1

        for i in range(1, x+1):
            bazinga = bazinga * i
    
    return bazinga

print(factOrSum(5,"factorial"))

