#Scopes are those variables or memory blocks which can be accessed by any class or functions


x=1

def add(y):
    global x
    x=2
    return x+y


print(add(4))