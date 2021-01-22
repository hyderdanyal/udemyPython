friends = []

def hello():
    friends.append("Rolf")
hello()
print(friends)

def add(x, y=8):
    result = x + y
    print(result)
add(5, 7)

#dict destructuring
nums = {"x": 15, "y": 25}
print(add(**nums))

def sub(x, y):
    return x - y
res = sub(5, 2)
print(res)

#lambda function
#lambda x, y : x + y
print((lambda x, y: x + y)(5, 7))

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
#doubled = [double(x) for x in sequence] #listcomprehension
doubled = list(map(double, sequence))
doubledd = list(map((lambda x: x * 2), sequence))
print(doubledd)
print(doubled)

