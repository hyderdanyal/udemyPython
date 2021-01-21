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