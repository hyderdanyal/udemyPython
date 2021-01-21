day_of_week = input("Enter a day:").lower()

if day_of_week == "monday":
    print("Monday")
elif day_of_week == "tuesday":
    print("Tuesday")
else:
    print("Not Monday")

friends = ["Ross", "Taylor", "Joe"]
#if "Joe" in friends:
if "Joe" in {"Kabir","Aziz","Asma"}:
    print("Joe is present")
else:
    print("Absent")

search = input("What do you wanna search?")
while search in friends:
    print("Present")
    search = input("Do you wanna check someone else")

#for friend in friends:
for friend in range(4):
    print(f"{friend} is my friend")