
#forloop
siblings = ["skye", "kyra", "dane"]

for name in siblings:
    print(name)

print(siblings)

# boolean

name = input("name a sibling?\n")
# gives it a line break if you use \n
isBest = "skye" == name.lower()

if isBest: 
    print("is the best sibling")
else:
    print("is not the best sibling")


