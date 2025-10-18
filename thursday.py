def greet(name):
    print("Hello " + name)
if name == "Bob":
    print("Welcome back, Bob!")
else:
    print("Nice to meet you!")

guests = ["Alice", "Bob", "Charlie"]
for guest in guests:
    greet(guest)

if guest == "Charlie":
    print("Glad you could join us!")