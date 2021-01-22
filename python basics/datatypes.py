x = 15 #int
price = 9.99 #float
discount = 0.2
result = price * (1-discount)
print(result)

#name = "Rolf" #string
name = input("Enter your name:") #input
print(name * 2)
greeting = f"Hello, {name}"
print(greeting)
date = input("Enter a year in numbers:")
date = int(date) #type casting
date = date - 2000
greetings = "Hello, {}. Today is {} year from 2000"
with_name = greetings.format(name, date)
#with_name = greetings.format("David")
print(with_name)

a = 25
b = a
b = 17
print(a, b)

print("test")
var1 = var2 = 5
print(var1, var2)
num1 = 8
num2 = 2
print(num1 * num2)

li = [2, 3, 4] #list
tu = (2, 3, 3) #tuple
se = {2, 3, 4} #set
li[0]= "Smith"
li.append(7)
#li.remove(li[0])
li.remove(7)
print(li)
se.add(9)
se.add(9) #can't allow duplicates won't add won't cause error
print(se)

friends = {"Bob", "Mary", "Anne"}
abroad = {"Bob", "Mary"}
local = friends.difference(abroad)
brother = {"Cammie", "Bob"}
print(local)
fandf = friends.union(brother)
print(fandf)
both = friends.intersection(brother)
print(both)

print(5 == 5)#boolean
print(5 != 5)

#list comprehensions
numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]
print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
start_s = [friend for friend in friends if friend.startswith("S")]
print(start_s)

friend_age = {"Rolf": 24, "Adam": 30, "Anne": 27} #dicionary
friend_age["Bob"] = 20
print(friend_age["Bob"])
for name in friend_age:
    print(f"{name}:{friend_age[name]}")
for name,age in friend_age.items():
    print(f"{name}:{age}")

#list of dict
friends = [
    {"name": "Rolf", "age": 20},
    {"name": "James", "age": 30}
]
print(friends[1]["name"])

#destructuring variables
t = 5, 11
_, y = t
print(y)
*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)

#destructuring dictionary
nums = {"x":15,"y":25}
print(**nums)
